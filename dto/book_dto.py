from datetime import datetime


class BookDTO:
    def __init__(
        self,
        id=None,
        title=None,
        isbn=None,
        category_name=None,
        publisher_name=None,
        publish_year=None,
        created_at=None,
        category_id=None,
        publisher_id=None,
    ):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.category_name = category_name
        self.publisher = publisher_name
        self.publish_year = publish_year
        self.created_at = created_at or datetime.now()
        self.category_id = category_id
        self.publisher_id = publisher_id

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "isbn": self.isbn,
            "category": self.category,
            "publisher_name": self.publisher_name,
            "publish_year": self.publish_year,
            "created_at": self.created_at,
            "category_id": self.category_id,
            "publisher_id": self.publisher_id,
        }
