import multiprocessing


def task(queue):
    value = queue.get()
    print(
        f'Process {multiprocessing.current_process().pid} popped {value} from the shared Queue')
    queue.task_done()


def main():
    manager = multiprocessing.Manager()
    q = manager.Queue()
    q.put(2)
    q.put(3)
    q.put(4)

    processes = []

    for _ in range(3):
        process = multiprocessing.Process(target=task, args=(q, ))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()

'''
Process 3935 popped 2 from the shared Queue
Process 3936 popped 3 from the shared Queue
Process 3937 popped 4 from the shared Queue
'''
