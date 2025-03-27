Было произведено тестирование класса BooksCollector из файла main.py.
Для тестирования были созданы методы:
1) test_books_genre_is_dictionary_true: 
Проверяет, что при инициализации класса BooksCollector атрибут books_genre является пустым словарем
2) test_books_favorites_is_list_true:
Проверяет, что при инициализации класса BooksCollector атрибут favorites является пустым списком.
3) test_default_books_genre_true:
Проверяет, что при инициализации класса BooksCollector атрибут genre содержит заданный список жанров.
4) test_default_books_genre_age_rating_true:
Проверяет, что при инициализации класса BooksCollector атрибут genre_age_rating содержит заданный список жанров для взрослой аудитории.
5) test_add_new_book_valid_name_true:
Проверяет, что можно добавить новую книгу с валидным именем (длина от 1 до 40 символов) без указания жанра.
6) test_add_new_book_invalid_len_name_true: 
Проверяет, что при попытке добавить книгу с невалидным именем (пустое имя или длина больше 40 символов) коллекция книг не изменяется.
7) test_set_book_genre_valid_genre:
Проверяет, что можно установить жанр для книги с валидным именем.
8) test_set_book_genre_invalid_genre:
Проверяет, что попытка установить невалидный жанр для книги не изменяет существующий жанр.
9) test_get_book_genre_valid_genre: 
Проверяет, что можно получить жанр существующей книги.
10) test_get_book_genre_non_existing_book:
Проверяет, что при запросе жанра несуществующей книги возвращается None.
11) test_get_books_with_specific_genre_valid_genre: 
Проверяет, что метод возвращает список книг для заданного жанра, если книги существуют.
12) test_get_books_with_specific_genre_invalid_genre:
Проверяет, что метод возвращает пустой список, если запрашиваемый жанр не существует.
13) test_get_books_with_specific_genre_empty_book:
Проверяет, что метод возвращает пустой список, если для запрашиваемого жанра нет книг.
14) test_get_books_genre_is_correct: 
Проверяет, что жанр книги правильно устанавливается и возвращается.
15) test_get_books_for_children_true_genre: 
Проверяет, что метод возвращает список книг, подходящих для детей.
16) test_add_book_in_favorites_new_book:
Проверяет, что новая книга может быть добавлена в избранное.
17) test_delete_book_from_favorites_existing_book:
Проверяет, что существующая книга может быть удалена из избранного.
18) test_get_list_of_favorites_books_true:
Проверяет, что метод возвращает правильный список избранных книг.

Для работы с тестовыми методами был создан файл conftest.py в котором содержатся фикстуры для создания объектов класса