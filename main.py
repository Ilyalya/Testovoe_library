import psycopg2
from datetime import timedelta
from contextlib import closing
from collections import Counter

students = []

validity = timedelta(days=30)

with closing(psycopg2.connect(database="testovoe",
  user="postgres",
  password="1234",
  host="localhost",
  port="5432")) as conn:

    with conn.cursor() as cursor:
        cursor.execute('select form.date_of_issue, form.date_of_return, students.full_name from form join students on form.student = students.student_id join books on form.book = books.book_id order by full_name')
        for row in cursor:
            if (row[1] - row[0]) > validity:
                students.append(row[2])

for i in range(len(Counter(students).most_common())):
    count = max(Counter(students).most_common(), key=lambda x: x[1])

print(count[0], "не вернул или вернул книги позже срока", count[1], "раз")