# Работа с базой данных, используя библиотеку psycopg2

*create_table_students(host, db_name)* -- создаёт таблицу студентов со следующими полями:
ID, surname, name, age

*create_table_marks(host, db_name)* -- создаёт таблицу оценок со следующими полями:
ID(студента), mark_1, mark_2, mark_3, mark_4, mark_5

*fill_table_students(data, host, db_name)* -- заполнение таблицы студентов данными data,
где data -- вектора из трех компонент(name, surname, age), поле ID -- генерируется автоматически

*fill_table_marks(data, host, db_name)* -- заполнение таблицы оценок данными data,
где data -- вектора из шести компонент(ID, mark_{1, 2, 3, 4, 5})

Получение средней оценки каждого студента -- *get_average(host, db_name)*

Вывод гистограммы с используя matplotlib -- *show_hist(sample)*, где sample --
вектор средних оценок студентов
