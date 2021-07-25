import pymysql


def connect_database():
    connect = pymysql.connect(
        host='10.8.0.22',
        port=3306,
        user='tc_test1_ats',
        password='tc_test1_ats#passwd',
        database='test1_ats',
        charset='utf8'
    )

    cursor = connect.cursor()
    return cursor


def operate():
    sql = 'insert into student (name, age) values(%s,%s);'

    data = [
        ('张三', '22'),
        ('李四', '23')
    ]
    connect_database.cursor.executemany(sql, data)
    connect_database.connect.commit()

    connect_database.cursor.execute('SELECT * FROM student')
    print(connect_database.cursor.fetchall())
    connect_database.cursor.close()
    connect_database.connect.close()


if __name__ == '__main__':
    connect_database()
    operate()
