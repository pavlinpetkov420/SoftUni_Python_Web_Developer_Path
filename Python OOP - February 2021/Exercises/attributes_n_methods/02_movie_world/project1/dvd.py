from datetime import datetime


class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {self.status(self.is_rented)}"

    @staticmethod
    def status(is_rented):
        if is_rented:
            return "rented"
        return "not rented"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date_obj = datetime.strptime(date, "%d.%m.%Y")
        date_f = date_obj.strftime("%d.%B.%Y")
        date_l = date_f.split('.')
        month_w_str = date_l[1]
        year_int = int(date_l[2])
        return cls(name, id, year_int, month_w_str, age_restriction)


