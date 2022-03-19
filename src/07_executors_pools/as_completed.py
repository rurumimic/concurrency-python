import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, URLError, urljoin, urlopen

URLS = [
    'https://www.google.com',
    'https://www.example.com',
    'https://github.com',
    'https://www.youtube.com',
]


def check_status(url):
    print(f'Attempting to crawl URL: {url}')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.getcode(), url


def print_status(status_code):
    print(f'URL Crawled with status code: {status_code}')


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = []

        for url in URLS:
            task = executor.submit(check_status, (url))
            tasks.append(task)

        for future in as_completed(tasks):
            print_status(future.result())


if __name__ == '__main__':
    main()

'''
Attempting to crawl URL: https://www.google.com
Attempting to crawl URL: https://www.example.com
Attempting to crawl URL: https://github.com
Attempting to crawl URL: https://www.youtube.com
URL Crawled with status code: (200, 'https://github.com')
URL Crawled with status code: (200, 'https://www.google.com')
URL Crawled with status code: (200, 'https://www.youtube.com')
URL Crawled with status code: (200, 'https://www.example.com')
'''
