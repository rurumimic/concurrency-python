import time
from multiprocessing import Pool


def task(n):
    time.sleep(n/8)
    print('*'*n)
    return n


def main():
    with Pool(4) as p:
        for iter in p.imap_unordered(task, [1, 2, 5, 8, 7, 3, 9, 4, 6]):
            print(iter)


if __name__ == '__main__':
    main()

'''
*
1
**
2
***
*****
3
5
********
*******
7
8
****
4
*********
******
9
6
'''

'''
1 *
2 **
3 ***
5 *****
7 ********
8 *******
4 ****
9 *********
6 ******
'''
