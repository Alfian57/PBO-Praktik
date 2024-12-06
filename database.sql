CREATE TABLE `students`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nis` CHAR(5) NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `phone_number` VARCHAR(25) NOT NULL,
    `address` TEXT NOT NULL,
    `class_id` BIGINT UNSIGNED NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE
    `students` ADD UNIQUE `students_nis_unique`(`nis`);
CREATE TABLE `admins`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE
    `admins` ADD UNIQUE `admins_email_unique`(`email`);
CREATE TABLE `books`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(100) NOT NULL,
    `isbn` CHAR(13) NOT NULL,
    `category_id` BIGINT UNSIGNED NOT NULL,
    `publisher_id` BIGINT UNSIGNED NOT NULL,
    `publish_year` YEAR NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE
    `books` ADD UNIQUE `books_isbn_unique`(`isbn`);
CREATE TABLE `book_loans`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `student_id` BIGINT UNSIGNED NOT NULL,
    `book_id` BIGINT UNSIGNED NOT NULL,
    `borrowing_date` DATE NOT NULL,
    `return_date` DATE NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE `categories`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE `class`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE `publishers`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE
    `books` ADD CONSTRAINT `books_category_id_foreign` FOREIGN KEY(`category_id`) REFERENCES `categories`(`id`);
ALTER TABLE
    `book_loans` ADD CONSTRAINT `book_loans_student_id_foreign` FOREIGN KEY(`student_id`) REFERENCES `students`(`id`);
ALTER TABLE
    `book_loans` ADD CONSTRAINT `book_loans_book_id_foreign` FOREIGN KEY(`book_id`) REFERENCES `books`(`id`);
ALTER TABLE
    `students` ADD CONSTRAINT `students_class_id_foreign` FOREIGN KEY(`class_id`) REFERENCES `class`(`id`);
ALTER TABLE
    `books` ADD CONSTRAINT `books_publisher_id_foreign` FOREIGN KEY(`publisher_id`) REFERENCES `publishers`(`id`);