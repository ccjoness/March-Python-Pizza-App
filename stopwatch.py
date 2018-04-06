import datetime
import time


class Stopwatch:
    def __init__(self, employee_id):
        #self.verify_employee_id()
        self.employee_id = employee_id
        #self.verify_clock_in()
        self.time_in = self.clock_in()
        self.time_out = datetime.time(0, 0)
        self.view_clock_in()

    # def verify_clock_in(self):
    #     manager_approval_req = True
    #     if self.time_in.strftime('%A') in Employer.schedule[employee_id]:
    #         try:
    #             for lst in Employer.schedule[employee_id][self.time_in.strftime('%A')]:
    #                 delta = lst[0] - self.time_in
    #                 if delta.minutes < 30:
    #                     manager_approval_req = False
    #         except IndexError:
    #             pass
    #     if manager_approval_req:
    #         while True:
    #             approval = input('Please enter manager ID for approval: ')
    #             if approval == Employer.ID:
    #                 break
    #
    # def verify_clock_out(self):
    #     manager_approval_req = True
    #     if self.time_out.strftime('%A') in Employer.schedule[employee_id]:
    #         try:
    #             for lst in Employer.schedule[employee_id][self.time_out.strftime('%A')]:
    #                 delta = lst[1] - self.time_out
    #                 if delta.minutes < 30:
    #                     manager_approval_req = False
    #         except IndexError:
    #             pass
    #     if manager_approval_req:
    #         while True:
    #             approval = input('Please enter manager ID for approval: ')
    #             if approval == Employer.ID:
    #                 break

    # def verify_employee_id(self):
    #     while self.employee_id not in Employer.crew:
    #         self.employee_id = input('Please enter your employee ID: ')



    def clock_in(self):
        time = datetime.datetime.now()
        return time

    def clock_out(self):
        #self.verify_clock_out()
        self.time_out = datetime.datetime.now()
        self.view_clock_out()

    def hours_worked(self):
        delta = self.time_in - self.time_out
        return delta

    def view_hours_worked(self):
        delta = self.time_in - self.time_out
        return delta.hours

    def view_clock_in(self):
        print(f'{self.employee_id} has been clocked in at:')
        print(self.time_in.strftime('%d-%b  %H:%M'))


    def view_clock_out(self):
        print(f'{self.employee_id} has been clocked out at:')
        print(self.time_in.strftime('%d-%b  %H:%M'))
        hours = self.view_hours_worked()
        print(f'Totaled {hours} hours today')


    #check timezone

if __name__ == '__main__':
    employee1 = Stopwatch('tj111')
    print('*'*40)
    print(employee1.time_out)