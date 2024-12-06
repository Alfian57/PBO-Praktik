from datetime import datetime


class BookReturnDTO:
    def __init__(
        self,
        id=None,
        book_loan_id=None,
        return_date=None,
        penalty_fee=None,
        created_at=None,
    ):
        self.id = id
        self.book_loan_id = book_loan_id
        self.return_date = return_date
        self.penalty_fee = penalty_fee
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "book_loan_id": self.book_loan_id,
            "return_date": self.return_date,
            "penalty_fee": self.penalty_fee,
            "created_at": self.created_at,
        }
