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


