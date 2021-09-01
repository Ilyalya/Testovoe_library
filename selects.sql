select form.date_of_issue, form.date_of_return, form.validity, students.full_name, books.name_of_book, books.full_name_of_authors
from form form
join students students on form.student = students.student_id
join books books on form.book = books.book_id
order by full_name