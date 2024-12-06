from datetime import datetime


class StudentDTO:
    def __init__(
        self,
        id=None,
        nis=None,
        name=None,
        phone_number=None,
        address=None,
        class_name=None,
        created_at=None,
        class_id=None,
    ):
        self.id = id
        self.nis = nis
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.class_name = class_name
        self.created_at = created_at or datetime.now()
        self.class_id = class_id

    def to_dict(self):
        return {
            "id": self.id,
            "nis": self.nis,
            "name": self.name,
            "phone_number": self.phone_number,
            "address": self.address,
            "class_name": self.class_name,
            "created_at": self.created_at,
            "class_id": self.class_id,
        }
