import pymysql

connect = pymysql.connect(
    host='10.8.0.22',
    port=3306,
    user='tc_test1_ats',
    password='tc_test1_ats#passwd',
    database='test1_ats',
    charset='utf8'
)
cursor = connect.cursor()
sql = 'insert into student (name, age) values(%s,%s);'

data = [
    ('张三', '22'),
    ('李四', '23')
]
cursor.executemany(sql, data)
connect.commit()

cursor.execute('SELECT * FROM student')
print(cursor.fetchall())
cursor.close()
connect.close()