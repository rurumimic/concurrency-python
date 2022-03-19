import multiprocessing
import os


class WorkerProcess(multiprocessing.Process):
    def __init__(self):
        super(WorkerProcess, self).__init__()

    def run(self):
        print(f'Child PID: {multiprocessing.current_process().pid}')


def main():
    print(f'Main PID: {multiprocessing.current_process().pid}')

    processes = []
    count = os.cpu_count()
    if count == None:
        return

    print(f'os.cpu: {count}')
    for i in range(count):
        process = WorkerProcess()  # 0
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()

'''
Main PID: 77701
os.cpu: 8

Child PID: 77714
Child PID: 77712
Child PID: 77713
Child PID: 77715

Child PID: 77716
Child PID: 77717
Child PID: 77718
Child PID: 77719
'''
