import sqlite3
from collections import namedtuple

from functional import seq

with sqlite3.connect(':memory:') as conn:
    conn.execute('CREATE TABLE user (id INT, name TEXT)')
    conn.commit()
    User = namedtuple('User', 'id name')

    seq([(1, 'pedro'), (2, 'fritz')]).to_sqlite3(
        conn, 'INSERT INTO user (id, name) VALUES (?, ?)')
    seq([(3, 'sam'), (4, 'stan')]).to_sqlite3(conn, 'user')
    seq([User(name='tom', id=5), User(name='keiga', id=6)]).to_sqlite3(conn, 'user')
    seq([dict(name='david', id=7), User(name='jordan', id=8)]
        ).to_sqlite3(conn, 'user')

    print(list(conn.execute('SELECT * FROM user')))
    # [
    #   (1, 'pedro'), (2, 'fritz'),
    #   (3, 'sam'), (4, 'stan'),
    #   (5, 'tom'), (6, 'keiga'),
    #   (7, 'david'), (8, 'jordan')
    # ]

    users = seq.sqlite3(conn, 'SELECT * FROM user').to_list()
    print(users)
