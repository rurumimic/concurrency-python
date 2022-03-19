import multiprocessing


def task(ns):
    print(ns.x)  # print 1
    ns.x = 2


def main():
    manager = multiprocessing.Manager()
    ns = manager.Namespace()
    ns.x = 1

    print(ns)  # Namespace(x=1)

    process = multiprocessing.Process(target=task, args=(ns, ))
    process.start()
    process.join()  # print 1

    print(ns)  # Namespace(x=2)


if __name__ == '__main__':
    main()
