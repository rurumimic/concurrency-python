import csv
import queue
import ssl
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from urllib.request import Request, URLError, urljoin, urlopen

from bs4 import BeautifulSoup  # pip install beautifulsoup4


class CheckableQueue(queue.Queue):  # or OrderedSetQueue
    def __contains__(self, item):
        with self.mutex:
            return item in self.queue

    def __len__(self):
        return len(self.queue)


THREAD_COUNT = 20
linksToCrawl = CheckableQueue()


class Page():
    def __init__(self, statusCode, requestTime, url):
        self.statusCode = statusCode
        self.requestTime = requestTime
        self.url = url


class Crawler:

    base_url = ''
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    crawledLinks = set()
    errorLinks = set()

    def __init__(self, base_url):
        Crawler.base_url = base_url
        Crawler.myssl = ssl.create_default_context()
        Crawler.myssl.check_hostname = False
        Crawler.myssl.verify_mode = ssl.CERT_NONE

    @staticmethod
    def crawl(thread_name, url, linksToCrawl):
        print(thread_name)
        try:
            link = urljoin(Crawler.base_url, url)
            if (urlparse(link).netloc == urlparse(Crawler.base_url).netloc) and (link not in Crawler.crawledLinks):
                request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                response = urlopen(request, context=Crawler.myssl)

                Crawler.crawledLinks.add(link)
                print(
                    f'> Url {response.geturl()} Crawled with Status: {response.getcode()} : {len(Crawler.crawledLinks)} Crawled In Total')

                soup = BeautifulSoup(response.read(), 'html.parser')
                Crawler.enqueueLinks(soup.find_all('a'), linksToCrawl)
                return url, response.getcode()
        except URLError as e:
            print(
                f'URL {link} threw this error when trying to parse: {e.reason}')
            Crawler.errorLinks.add(link)
            # raise Exception(f'URL {link} threw URLError: {e.reason}')
            return url, response.getcode()
        except Exception as e:
            Crawler.errorLinks.add(link)
            # raise Exception(f'URL {link} threw Exception: {e.reason}')
            return url, response.getcode()

    @ staticmethod
    def enqueueLinks(links, linksToCrawl):
        for link in links:
            if (urljoin(Crawler.base_url, link.get('href')) not in Crawler.crawledLinks):
                if (urljoin(Crawler.base_url, link.get('href')) not in linksToCrawl):
                    linksToCrawl.put(link.get('href'))


def run(url):
    try:
        result = Crawler.crawl(threading.current_thread(), url, linksToCrawl)
        linksToCrawl.task_done()
        return result
    except:
        raise Exception(f'Exception thrown with link: {url}')


def appendToCSV(result):
    print(f'{threading.current_thread()} Appending result to CSV File: {result}')
    with open('results.csv', 'a') as csvfile:
        resultwriter = csv.writer(
            csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        resultwriter.writerow(result)


def main():
    # url = input('Website > ')
    url = 'https://tutorialedge.net/'
    print(url)
    Crawler(url)
    linksToCrawl.put(url)
    while not linksToCrawl.empty():
        with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
            url = linksToCrawl.get()
            futures = []

            if url is not None:
                future = executor.submit(run, (url))
                futures.append(future)

            for future in as_completed(futures):
                try:
                    if future.result() != None:
                        appendToCSV(future.result())
                except:
                    print(future.exception())

    print(f'Total Links Crawled: {len(Crawler.crawledLinks)}')
    print(f'Total Errors: {len(Crawler.errorLinks)}')


if __name__ == '__main__':
    main()
