class Schedule:

    def __init__(self, id_number: str, hour_in: int, hour_out: int):
        self.id_number = id_number
        self.hour_in = hour_in
        self.hour_out = hour_out

    def get_hours(self) -> float:
        hours = self.hour_out - self.hour_in
        return hours

