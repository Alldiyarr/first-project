import pytest
from main import BooksCollector  # Импортируем наш класс

def test_add_new_book():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_genre()
