from dotenv import load_dotenv
from app.db import DB
from repository.class_repository import ClassRepository


def init():
    load_dotenv()


def main():
    classRepository = ClassRepository()
    classRepository.add("Math")


def cleanup():
    db = DB.get_instance()
    db.close()


if __name__ == "__main__":
    init()
    main()
    cleanup()
