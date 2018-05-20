import psycopg2
import matplotlib.pyplot as plt


def Create_table_students(host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE students(ID SERIAL PRIMARY KEY, name VARCHAR(30), surname VARCHAR(30), age INT)')
    cursor.close()
    conn.commit()
    conn.close()


def Create_table_marks(host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE marks(ID INT PRIMARY KEY ,mark_1 INT, mark_2 INT, mark_3 INT, mark_4 INT, mark_5 INT)')
    cursor.close()
    conn.commit()
    conn.close()


def Fill_table_students(data, host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()

    for i in data:
        cursor.execute("""
            INSERT INTO students(name, surname, age) 
            VALUES (%s, %s, %s)
            """, (i[0], i[1], i[2]))
    cursor.close()
    conn.commit()
    conn.close()


def Fill_table_marks(data, host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()

    for i in data:
        cursor.execute("""
            INSERT INTO marks 
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (i[0], i[1], i[2], i[3], i[4], i[5]))
    cursor.close()
    conn.commit()
    conn.close()


def Get_students(file):
    with open(file) as f:
        data = []
        for i in f.read().split('\n'):
            student = []
            for j in i.split():
                student.append(j)
            student[-1] = int(student[-1])
            data.append(student)
        return data


def Get_marks(file):
    with open(file) as f:
        data = []
        for i in f.read().split('\n'):
            marks = []
            for j in i.split():
                marks.append(int(j))
            data.append(marks)
        return data


def Get_average(host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5 from marks')
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return [i[0] for i in result]


def Show_hist(sample):
    plt.figure(figsize=(10, 4))
    plt.hist(sample, bins=8, alpha=0.4, color='orange')
    plt.xlabel('average')
    plt.ylabel('students')
    plt.grid(ls=':')
    plt.show()


Create_table_students('localhost', 'group_697')
Create_table_marks('localhost', 'group_697')
Fill_table_students(Get_students('students.txt'), 'localhost', 'group_697')
Fill_table_marks(Get_marks('marks.txt'), 'localhost', 'group_697')
Show_hist(Get_average('localhost', 'group_697'))