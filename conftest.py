import pytest as pytest

from main import BooksCollector


@pytest.fixture
def setup_books_collector():
    collector = BooksCollector()
    collector.add_new_book('Аватар')  # Добавляем книгу
    collector.add_new_book('Лучший сыщик')  # Добавляем книгу
    collector.set_book_genre('Аватар', 'Фантастика')  # Устанавливаем жанр
    collector.set_book_genre('Лучший сыщик', 'Детективы')  # Устанавливаем жанр
    return collector
