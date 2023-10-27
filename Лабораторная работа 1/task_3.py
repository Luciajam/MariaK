# TODO Найдите количество книг, которое можно разместить на дискете
Volume = 1.44
number_of_pages = 100
number_of_str = 50
number_of_simbols = 25
Volume = Volume * 1024 * 1024
Volume_of_books = 4 * number_of_simbols * number_of_str * number_of_pages
number_of_books = Volume / Volume_of_books
number_of_books = round(number_of_books)
print("Количество книг, помещающихся на дискету:", number_of_books)
