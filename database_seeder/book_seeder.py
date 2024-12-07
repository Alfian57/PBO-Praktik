from repository.book_repository import BookRepository
from dto.book_dto import BookDTO
import random


class BookSeeder:
    def __init__(self) -> None:
        self.book_repository = BookRepository()

    def get_data(self):
        return [
            {
                "title": "Laskar Pelangi",
                "isbn": "978-602-291-038-8",
                "publish_year": 2005,
            },
            {
                "title": "Sang Pemimpi",
                "isbn": "978-602-291-039-5",
                "publish_year": 2006,
            },
            {"title": "Edensor", "isbn": "978-602-291-040-1", "publish_year": 2007},
            {
                "title": "Maryamah Karpov",
                "isbn": "978-602-291-041-8",
                "publish_year": 2008,
            },
            {
                "title": "Cinta di Dalam Gelas",
                "isbn": "978-602-291-042-5",
                "publish_year": 2009,
            },
            {"title": "Rindu", "isbn": "978-602-291-043-2", "publish_year": 2011},
            {
                "title": "Padang Bulan",
                "isbn": "978-602-291-044-9",
                "publish_year": 2012,
            },
            {
                "title": "Cinta Brontosaurus",
                "isbn": "978-602-291-045-6",
                "publish_year": 2013,
            },
            {
                "title": "Museum Hantu",
                "isbn": "978-602-291-046-3",
                "publish_year": 2014,
            },
            {
                "title": "Sapiens: A Brief History of Humankind",
                "isbn": "978-0-06-231609-7",
                "publish_year": 2011,
            },
            {
                "title": "Homo Deus: A Brief History of Tomorrow",
                "isbn": "978-0-06-246431-6",
                "publish_year": 2015,
            },
            {
                "title": "21 Lessons for the 21st Century",
                "isbn": "978-0-525-51219-6",
                "publish_year": 2018,
            },
            {
                "title": "The Subtle Art of Not Giving a F*ck",
                "isbn": "978-0-06-245771-4",
                "publish_year": 2016,
            },
            {
                "title": "Atomic Habits",
                "isbn": "978-0-7352-1129-3",
                "publish_year": 2018,
            },
            {"title": "Educated", "isbn": "978-0-399-59050-4", "publish_year": 2018},
            {"title": "Becoming", "isbn": "978-1-5247-6313-8", "publish_year": 2018},
            {
                "title": "The Power of Habit",
                "isbn": "978-1-4000-6928-6",
                "publish_year": 2012,
            },
            {
                "title": "Thinking, Fast and Slow",
                "isbn": "978-0-374-53355-7",
                "publish_year": 2011,
            },
            {
                "title": "The Alchemist",
                "isbn": "978-0-06-112241-5",
                "publish_year": 1988,
            },
            {
                "title": "The Catcher in the Rye",
                "isbn": "978-0-316-76948-0",
                "publish_year": 1951,
            },
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.book_repository.add(
                BookDTO(
                    title=dto["title"],
                    isbn=dto["isbn"],
                    publish_year=dto["publish_year"],
                    publisher_id=random.randint(1, 22),
                    category_id=random.randint(1, 20),
                )
            )
