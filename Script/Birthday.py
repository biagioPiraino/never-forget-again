from datetime import datetime

class Birthday:
    def __init__(self, name: str, date: datetime, email: str) -> None:
        self.name  = name
        self.date  = date
        self.email = email