import pytest as pytest

from main import BooksCollector


@pytest.fixture
def setup_books_collector():
    collector = BooksCollector()
    collector.add_new_book('Аватар')
    collector.add_new_book('Лучший сыщик')
    collector.add_new_book('Солярис')
    collector.add_new_book('Три кота')
    collector.set_book_genre('Аватар', 'Фантастика')
    collector.set_book_genre('Солярис', 'Фантастика')
    collector.set_book_genre('Лучший сыщик', 'Детективы')
    collector.set_book_genre('Три кота', 'Мультфильмы')
    return collector


@pytest.fixture
def setup_books_collector_for_favorites_books():
    collector = BooksCollector()
    collector.add_new_book('Задача трех тел')
    collector.add_new_book('Первый кот на Луне')
    collector.add_new_book('Горе от ума')
    collector.set_book_genre('Задача трех тел', 'Фантастика')
    collector.set_book_genre('Первый кот на Луне', 'Фантастика')
    collector.set_book_genre('Горе от ума', 'Комедии')
    collector.add_book_in_favorites('Задача трех тел')
    collector.add_book_in_favorites('Горе от ума')
    return collector
