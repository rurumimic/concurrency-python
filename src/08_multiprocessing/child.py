import multiprocessing


class WorkerProcess(multiprocessing.Process):
    def __init__(self):
        super(WorkerProcess, self).__init__()
        print('Worker Process')  # 1

    def run(self):
        print(f'Child PID: {multiprocessing.current_process().pid}')  # 3.2


def main():
    print(f'Main PID: {multiprocessing.current_process().pid}')

    process = WorkerProcess()  # 0
    print('Created Worker Process')  # 2
    process.start()  # 3.1
    print('Started Worker Process')  # 4
    process.join()
    print('Worker Process finished')  # 5
    process.run()  # 6 == Main Process
    print('End')  # 7


if __name__ == '__main__':
    main()

'''
Main PID: 75344
Worker Process # 1
Created Worker Process # 2
Started Worker Process # 4
Child PID: 75355 # run
Worker Process finished # 5
Child PID: 75344 # 6
End # 7
'''
