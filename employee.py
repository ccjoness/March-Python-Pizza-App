# from typing import List
# from schedule import Schedule


# Diana
# class Employee:
#
#     def __init__(self, id_number: str, day: str, start: int, end: int, wage: int, schedule: List[Schedule]):
#         self.id_number = id_number
#         self.day = day
#         self.start = start
#         self.end = end
#         self.wage = wage
#         self.schedule = schedule
#
#     def set_schedule(self, new_schedule: List[Schedule]):
#         self.schedule = new_schedule
#
#     def print_schedule(self) -> None:
#         list_of_schedules = self.schedule
#         for schedule in list_of_schedules:
#             print("Start: " + schedule.hour_in + " End: " + schedule.hour_out)
#
#     def print_hours_worked(self) -> None:
#         list_of_schedules = self.schedule
#         for schedule in list_of_schedules:
#             print(schedule.get_hours())
#
#     def calculated_wages(self) -> float:
#         list_of_schedules = self.schedule
#         for schedule in list_of_schedules:
#             return schedule.get_hours() * self.wage



class Employee:
    def __init__(self, name, emp_id, wage_code=0):
        self.name = name
        self.id = emp_id
        self.wage = wage_dict[wage_code]

    def dispatch(self, driver_id, order_id):
        driver_list.remove(driver_id)
        dispatch_pair = {driver_id: order_id}
        dispatch_dict.update(dispatch_pair)
        return '{} has assigned order number {} to driver {}.'.format(self.name, order_id, driver_id),

    def set_wage(self, wagecode):
        self.wage = wage_dict[wagecode]
        return "New Wage: {}".format(wage_dict[wagecode])


def gen_id():
    last_id = id_list.pop()
    new_id = last_id + 1
    id_list.append(last_id)
    id_list.append(new_id)
    return new_id


wage_dict = {0: 11.25, 1: 12.50, 2: 15.50, 3: 14.75, 4: 13.25}
if __name__ == '__main__':
    id_list = [0, 1]
    order_list = []
    driver_list = []
    wage_dict = {0: 11.25, 1: 12.50, 2: 15.50, 3: 14.75, 4: 13.25, 5: 25.25}
    dispatch_dict = {}
    TestEmp = Employee('Sullivan', gen_id())
    TestEmp.setwage(1)
    print(TestEmp.name, TestEmp.id, TestEmp.wage)
