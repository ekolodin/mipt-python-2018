import psycopg2
import argparse
import matplotlib.pyplot as plt


def create_table_students(host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE students(ID SERIAL PRIMARY KEY, name VARCHAR(30),
        surname VARCHAR(30), age INT)
        """)
    cursor.close()
    conn.commit()
    conn.close()


def create_table_marks(host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE marks(ID INT PRIMARY KEY, mark_1 INT,
        mark_2 INT, mark_3 INT, mark_4 INT, mark_5 INT)
        """)
    cursor.close()
    conn.commit()
    conn.close()


def fill_table_students(data, host, db_name):
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


def fill_table_marks(data, host, db_name):
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


def get_students(link):
    with open(link) as f:
        data = []
        try:
            for i in f.read().split('\n'):
                student = []
                for j in i.split():
                    student.append(j)
                student[-1] = int(student[-1])
                data.append(student)
            return data
        except ValueError:
            print('Incorrect input')


def get_marks(link):
    with open(link) as f:
        data = []
        try:
            for i in f.read().split('\n'):
                marks = []
                for j in i.split():
                    marks.append(int(j))
                data.append(marks)
            return data
        except ValueError:
            print('Incorrect input')


def get_average(host, db_name):
    conn = psycopg2.connect(host=host, dbname=db_name)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5
        from marks
        """)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return [i[0] for i in result]


def show_hist(sample):
    plt.figure(figsize=(10, 4))
    plt.hist(sample, bins=8, alpha=0.4, color='orange')
    plt.xlabel('average')
    plt.ylabel('students')
    plt.grid(ls=':')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--students_file', required=True, dest='students', help='path to load students')
    parser.add_argument('--marks_file', required=True, dest='marks', help='path to load marks')
    parser.add_argument('--host', required=True, dest='host', help='host')
    parser.add_argument('--database', required=True, dest='database', help='name of database')

    args = parser.parse_args()
    create_table_students(args.host, args.database)
    create_table_marks(args.host, args.database)
    fill_table_students(get_students(args.students), args.host, args.database)
    fill_table_marks(get_marks(args.marks), args.host, args.database)
    show_hist(get_average(args.host, args.database))
