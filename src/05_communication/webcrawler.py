import queue
import ssl
import threading
from ast import Pass
from urllib.parse import urlparse
from urllib.request import Request, URLError, urljoin, urlopen

from bs4 import BeautifulSoup  # pip install beautifulsoup4


class CheckableQueue(queue.Queue):
    def __contains__(self, item):
        with self.mutex:
            return item in self.queue

    def __len__(self):
        return len(self.queue)


class Crawler(threading.Thread):

    def __init__(self, baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock=None):
        threading.Thread.__init__(self)

        print(f'Web Crawler Worker Started: {threading.current_thread()}')

        self.baseUrl = baseUrl
        self.linksToCrawl = linksToCrawl
        self.haveVisited = haveVisited
        self.errorLinks = errorLinks
        self.urlLock = urlLock

    def run(self):
        myssl = ssl.create_default_context()
        myssl.check_hostname = False
        myssl.verify_mode = ssl.CERT_NONE

        while True:
            # self.urlLock.acquire()
            print(f'Queue size: {self.linksToCrawl.qsize()}')
            link = self.linksToCrawl.get()
            # self.urlLock.release()

            if link is None:
                print('link is none')
                break

            if (link in self.haveVisited):
                print(f'Already visited: {link}')
                break

            try:
                link = urljoin(self.baseUrl, link)
                req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                response = urlopen(req, context=myssl)

                print(
                    f'URL {response.geturl()} crawled with status: {response.getcode()}')

                soup = BeautifulSoup(response.read(), 'html.parser')

                for atag in soup.find_all('a'):
                    if (atag.get('href') not in self.haveVisited) and (urlparse(link).netloc == 'tutorialedge.net'):
                        self.linksToCrawl.put(atag.get('href'))
                    else:
                        print(
                            f'{atag.get("href")} already visited or not part of website.')

                print(f'Adding {link} to crawled list')
                self.haveVisited.append(link)
            except URLError as e:
                print(
                    f'URL {link} threw this error when trying to parse: {e.reason}')
                self.errorLinks.append(link)
            finally:
                self.linksToCrawl.task_done()


def main():

    print('Starting our Web Crawler')
    print('https://tutorialedge.net/')
    baseUrl = input('Website > ')
    numberOfThreads = input('No Threads > ')

    linksToCrawl = CheckableQueue()
    # urlLock = threading.Lock()
    urlLock = None
    linksToCrawl.put(baseUrl)

    haveVisited = []
    crawlers = []
    errorLinks = []

    for i in range(int(numberOfThreads)):
        crawler = Crawler(baseUrl, linksToCrawl,
                          haveVisited, errorLinks, urlLock)
        crawler.daemon = True
        crawler.start()
        crawlers.append(crawler)

    for crawler in crawlers:
        crawler.join()

    print(f'Total Number of Pages Visited {len(haveVisited)}')
    print(f'Total Number of Pages with Errors {len(errorLinks)}')


if __name__ == '__main__':
    main()

'''
Total Number of Pages Visited 70
Total Number of Pages with Errors 3
'''
