import threading
import time


def standard_thread():
    print('Start: Standard Thread')
    time.sleep(20)
    print('End: Standard Thread')


def daemon_thread():
    while True:
        print('Heartbeat Signal')
        time.sleep(2)


if __name__ == '__main__':
    standard_t = threading.Thread(target=standard_thread)
    daemon_t = threading.Thread(target=daemon_thread)
    daemon_t.daemon = True
    daemon_t.start()

    standard_t.start()
