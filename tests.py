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
        #Добавление книги без указания жанра с валидной длинной
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


