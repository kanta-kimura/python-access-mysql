import MySQLdb

import const


def access_db():
    """DBにアクセスする
    """

    conn = MySQLdb.connect(
        host=const.HOST,
        port=const.PORT,
        user=const.USER,
        passwd=const.PASSWORD,
        db=const.DATABASE,
        charset=const.CHARSET
    )

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    access_db()
