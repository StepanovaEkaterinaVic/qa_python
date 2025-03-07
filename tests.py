import pytest
from main import BooksCollector


class TestBooksCollector:

    # Тестирование метода __init__ класса BooksCollector

    def test_books_genre_is_dictionary_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_books_favorites_is_list_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_default_books_genre_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_default_books_genre_age_rating_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Тестирование метода add_new_book
    # Добавление книги без указания жанра с валидной длинной
    @pytest.mark.parametrize('book_name', ['A', 'B' * 10, 'c' * 40])
    def test_add_new_book_valid_name_true(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.books_genre == {book_name: ''}

        # Добавление книги без указания жанра с невалидной длинной

    @pytest.mark.parametrize('book_name', ['', 'B' * 41, 'c' * 50])
    def test_add_new_book_invalid_len_name_true(self, book_name):
        collector = BooksCollector()
        initial_books_genre = collector.books_genre.copy()
        collector.add_new_book(book_name)
        assert collector.books_genre == initial_books_genre

    # Тестирование метода set_book_genre
        # Установка валидного жанра
    @pytest.mark.parametrize('name', ['Задача трех тел'])
    def test_set_book_genre_valid_genre(self, name):
        collector = BooksCollector()
        genre = collector.genre[0]
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre == {name: genre}

        # Установка невалидного жанра

    @pytest.mark.parametrize('name, invalid_genre', [('Репка', 'Садоводство')])
    def test_set_book_genre_invalid_genre(self, name, invalid_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        original_genre = collector.books_genre.get(name)
        collector.set_book_genre(name, invalid_genre)
        assert collector.books_genre[name] == original_genre

        # Тестирование метода get_book_genre
            # Использование валидного жанра

    def test_get_book_genre_valid_genre(self, setup_books_collector):
        collector = setup_books_collector
        genre = collector.get_book_genre('Аватар')
        assert genre == 'Фантастика'

        # Узнать жанр несуществующей книги
    def test_get_book_genre_non_existing_book(self, setup_books_collector):
        collector = setup_books_collector
        genre = collector.get_book_genre('Неизвестная книга')
        assert genre is None

    # Тестирование метода get_books_with_specific_genre
        # Проверяем, что выводятся книги определенного жанра
    def test_get_books_with_specific_genre_valid_genre(self, setup_books_collector):
        collector = setup_books_collector
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Аватар', 'Солярис']

        # Проверяем, что возвращается пустой список, если такого жанра нет
    def test_get_books_with_specific_genre_invalid_genre(self, setup_books_collector):
        collector = setup_books_collector
        books = collector.get_books_with_specific_genre('Романы')
        assert books == []

        # Проверяем, что возвращается пустой список, если нет книг такого жанра
    def test_get_books_with_specific_genre_empty_book(self, setup_books_collector):
        collector = setup_books_collector
        books = collector.get_books_with_specific_genre('Комедии')
        assert books == []
