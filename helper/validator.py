import datetime


class Validator:
    @staticmethod
    def validate(data: dict, rules: dict, name: dict) -> str:
        for key, rule_list in rules.items():
            value = data.get(key, None)
            for rule in rule_list:
                error_message = rule(value)
                if error_message:
                    return f"{name[key]}: {error_message}"
        return None

    @staticmethod
    def email(email: str) -> str:
        is_valid = "@" in email and "." in email
        if not is_valid:
            return "tidak valid!"

    @staticmethod
    def max_length(max_length: int):
        def validate(value: str) -> str:
            is_valid = len(value) <= max_length
            if not is_valid:
                return f"Panjang karakter maksimal {max_length}"

        return validate

    @staticmethod
    def min_length(min_length: int):
        def validate(value: str) -> str:
            is_valid = len(value) >= min_length
            if not is_valid:
                return f"Panjang karakter minimal {min_length}"

        return validate

    @staticmethod
    def length(length: int):
        def validate(value: str) -> str:
            is_valid = len(value) == length
            if not is_valid:
                return f"Panjang karakter harus {length}"

        return validate

    @staticmethod
    def required(value: str) -> str:
        is_valid = value != ""
        if not is_valid:
            return "tidak boleh kosong!"

    @staticmethod
    def date(date: str) -> str:
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return "tidak valid!"

    @staticmethod
    def positive_integer(value: int) -> str:
        is_valid = value > 0
        if not is_valid:
            return "harus bilangan bulat positif!"

    @staticmethod
    def year(year: str) -> str:
        try:
            datetime.datetime.strptime(year, "%Y")
        except ValueError:
            return "tidak valid!"

    @staticmethod
    def date_after_today(date: str) -> str:
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            if date < datetime.datetime.now():
                return "tidak boleh sebelum hari ini!"
        except ValueError:
            return "tidak valid!"

    @staticmethod
    def date_after(reference_date: str):
        def validate(date: str) -> str:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            reference_date_new = datetime.datetime.strptime(reference_date, "%Y-%m-%d")
            if date < reference_date_new:
                return f"tidak boleh sebelum {reference_date_new.strftime('%d %B %Y')}!"

        return validate
