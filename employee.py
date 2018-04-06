from typing import List
from schedule import Schedule


class Employee:

    def __init__(self, id_number: str, day: str, start: int, end: int, wage: int, schedule: List[Schedule]):
        self.id_number = id_number
        self.day = day
        self.start = start
        self.end = end
        self.wage = wage
        self.schedule = schedule

    def set_schedule(self, new_schedule: List[Schedule]):
        self.schedule = new_schedule

    def print_schedule(self) -> None:
        list_of_schedules = self.schedule
        for schedule in list_of_schedules:
            print("Start: " + schedule.hour_in + " End: " + schedule.hour_out)

    def print_hours_worked(self) -> None:
        list_of_schedules = self.schedule
        for schedule in list_of_schedules:
            print(schedule.get_hours())

    def calculated_wages(self) -> float:
        list_of_schedules = self.schedule
        for schedule in list_of_schedules:
            return schedule.get_hours() * self.wage
