#!/usr/bin/python2
import multiprocessing
import os


class ChildProcess(multiprocessing.Process):
    def __init__(self, pipein):
        super(ChildProcess, self).__init__()
        self.pipein = pipein

    def run(self):
        print('Attempting to pipein to pipe')
        self.pipein = os.fdopen(self.pipein, 'w')
        self.pipein.write('My Name is Elon')
        self.pipein.close()


def main():
    pipeout, pipein = os.pipe()

    child = ChildProcess(pipein)
    child.start()
    child.join()

    os.close(pipein)
    pipeout = os.fdopen(pipeout)
    print('Pipe:', pipeout.read())


if __name__ == '__main__':
    main()
