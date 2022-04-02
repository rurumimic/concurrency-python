import gevent
from gevent import socket


def main():
    urls = ['www.google.com', 'www.example.com', 'www.python.org']
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=2)
    print([job.value for job in jobs])


if __name__ == '__main__':
    main()

'''
# sleep 2
['142.250.66.132', '93.184.216.34', '146.75.48.223']
'''
