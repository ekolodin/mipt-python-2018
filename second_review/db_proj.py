import psycopg2
import argparse


def create_table_students(host, db_name):
    with psycopg2.connect(host=host, dbname=db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE students(ID SERIAL PRIMARY KEY, name VARCHAR(30),
                surname VARCHAR(30), age INT)
                """)
        conn.commit()


def create_table_marks(host, db_name):
    with psycopg2.connect(host=host, dbname=db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE marks(ID INT PRIMARY KEY, mark_1 INT,
                mark_2 INT, mark_3 INT, mark_4 INT, mark_5 INT)
                """)
        conn.commit()


def fill_table_students(data, host, db_name):
    with psycopg2.connect(host=host, dbname=db_name) as conn:
        with conn.cursor() as cursor:
            for line in data:
                if len(line) != 3:
                    print('Incorrect input: {}'.format(line))
                else:
                    cursor.execute("""
                        INSERT INTO students(name, surname, age)
                        VALUES (%s, %s, %s)
                        """, (line[0], line[1], line[2]))
        conn.commit()


def fill_table_marks(data, host, db_name):
    with psycopg2.connect(host=host, dbname=db_name) as conn:
        with conn.cursor() as cursor:
            for line in data:
                if len(line) != 6:
                    print('Incorrect input: {}'.format(line))
                else:
                    cursor.execute("""
                        INSERT INTO marks
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """, (line[0], line[1], line[2],
                              line[3], line[4], line[5]))
        conn.commit()


def get_students(link):
    with open(link) as file:
        data = []
        for i in file.read().split('\n'):
            student = []
            for j in i.split():
                student.append(j)
            try:
                student[-1] = int(student[-1])
            except ValueError:
                print('Cannot cast {} to int'.format(student[-1]))
                return
            data.append(student)
        return data


def get_marks(link):
    with open(link) as file:
        data = []
        for line in file.read().split('\n'):
            try:
                marks = list(map(int, line.split()))
            except ValueError:
                print('Cannot cast {} to int'.format(line.split()))
                return
            data.append(marks)
        return data


def get_average(host, db_name):
    with psycopg2.connect(host=host, dbname=db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5
                from marks
                """)
            result = cursor.fetchall()
        conn.commit()
        return [str(i[0]) for i in result]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--students_file', required=True,
                        dest='students', help='path to load students')
    parser.add_argument('--marks_file', required=True,
                        dest='marks', help='path to load marks')
    parser.add_argument('--host', required=True, dest='host', help='host')
    parser.add_argument('--database', required=True,
                        dest='database', help='name of database')
    parser.add_argument('--load_file', required=True,
                        dest='averages', help='path to write averages')

    args = parser.parse_args()
    create_table_students(args.host, args.database)
    create_table_marks(args.host, args.database)
    fill_table_students(get_students(args.students), args.host, args.database)
    fill_table_marks(get_marks(args.marks), args.host, args.database)
    with open(args.averages, 'w') as f:
        f.write(' '.join(get_average(args.host, args.database)))
