import multiprocessing
import os
import sys


class ChildProcess(multiprocessing.Process):
    def __init__(self, pipein):
        super(ChildProcess, self).__init__()
        self.pipein = pipein

    def run(self):
        try:
            raise Exception('This broke stuff')
        except:
            except_type, except_class, tb = sys.exc_info()
            print('Attempting to pipein to pipe')
            self.pipein = os.fdopen(self.pipein, 'w')
            self.pipein.write(str(except_type))
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

'''
Attempting to pipein to pipe
('Pipe:', "<type 'exceptions.Exception'>")
'''
