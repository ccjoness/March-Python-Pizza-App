from schedule import Schedule


class Employer:

    def __init__(self, id_number: str, day: str, start: int, end: int):
        self.id_number = id_number
        self.day = day
        self.start = start
        self.end = end

    def print_schedule(self) -> None:
        list_of_schedules = self.schedule
        for schedule in list_of_schedules:
            print("Start: " + schedule.hour_in + " End: " + schedule.hour_out)