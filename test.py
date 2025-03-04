import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book(collector):
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_genre()

def test_add_new_book_with_long_name(collector):
    collector.add_new_book("А" * 41)  # Длина 41 символ, должно быть проигнорировано
    assert "А" * 41 not in collector.get_books_genre()

def test_set_book_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

def test_set_invalid_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Роман")  # Такого жанра нет в списке
    assert collector.get_book_genre("Гарри Поттер") == ""  # Должно остаться пустым

def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    collector.add_new_book("Властелин Колец")
    collector.set_book_genre("Властелин Колец", "Фантастика")

    assert set(collector.get_books_with_specific_genre("Фантастика")) == {"Гарри Поттер", "Властелин Колец"}

def test_get_books_for_children(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    collector.add_new_book("Пила")
    collector.set_book_genre("Пила", "Ужасы")  # Ужасы - для взрослых

    assert collector.get_books_for_children() == ["Гарри Поттер"]  # Только книги без 18+

def test_add_book_in_favorites(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_list_of_favorites_books()

def test_add_nonexistent_book_to_favorites(collector):
    collector.add_book_in_favorites("Несуществующая книга")
    assert "Несуществующая книга" not in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
    assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Властелин Колец")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.add_book_in_favorites("Властелин Колец")

    assert set(collector.get_list_of_favorites_books()) == {"Гарри Поттер", "Властелин Колец"}
