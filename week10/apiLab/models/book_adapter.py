from models.book import Book

class BookAdapter:
    def select_attributes(self, book):
        return {
            'id': book['key'],
            'title': book['title'],
            'author_name': book['author_name'],
            'published': book['first_publish_year']
        }
    
    def run(self, books):
        books_list = []
        for book in books:
            book_attrs = self.select_attributes(book)
            book_obj = Book(**book_attrs)
            books_list.append(book_obj)
        return books_list
    