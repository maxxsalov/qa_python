class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        assert len(collector.get_books_genre()) == 5

    def test_get_book_genre_check_genre(self, collector):
        assert collector.get_book_genre('Дюна')

    def test_get_books_genre(self, collector):
        assert collector.get_books_genre()

    def test_get_books_with_specific_genre(self, collector):
        assert collector.get_books_with_specific_genre('Детективы')

    def test_get_books_for_children(self, collector):
        assert collector.get_books_for_children()

    def test_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Пуаро')
        collector.add_book_in_favorites('Дюна')
        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Пуаро')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books(self, collector):
        collector.add_book_in_favorites('Пуаро')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books()
