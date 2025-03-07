import pytest as pytest

from main import BooksCollector


@pytest.fixture
def setup_books_collector():
    collector = BooksCollector()
    collector.add_new_book('Аватар')
    collector.add_new_book('Лучший сыщик')
    collector.add_new_book('Солярис')
    collector.set_book_genre('Аватар', 'Фантастика')
    collector.set_book_genre('Солярис', 'Фантастика')
    collector.set_book_genre('Лучший сыщик', 'Детективы')
    return collector

