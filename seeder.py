from database_seeder.admin_seeder import AdminSeeder
from database_seeder.category_seeder import CategorySeeder
from database_seeder.publisher_seeder import PublisherSeeder
from database_seeder.class_seeder import ClassSeeder
from database_seeder.student_seeder import StudentSeeder
from database_seeder.book_seeder import BookSeeder
from database_seeder.book_loan_seeder import BookLoanSeeder
from dotenv import load_dotenv


def main():
    load_dotenv()

    admin_seeder = AdminSeeder()
    category_seeder = CategorySeeder()
    publisher_seeder = PublisherSeeder()
    class_seeder = ClassSeeder()
    student_seeder = StudentSeeder()
    book_seeder = BookSeeder()
    book_loan_seeder = BookLoanSeeder()

    admin_seeder.run()
    category_seeder.run()
    publisher_seeder.run()
    class_seeder.run()
    student_seeder.run()
    book_seeder.run()
    book_loan_seeder.run()

    print("Seeder sukses!")


if __name__ == "__main__":
    main()
