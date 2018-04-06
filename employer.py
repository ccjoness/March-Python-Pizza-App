# from schedule import Schedule
#
#
# class Employer:
#
#     def __init__(self, id_number: str, day: str, start: int, end: int):
#         self.id_number = id_number
#         self.day = day
#         self.start = start
#         self.end = end
#
#     def print_schedule(self) -> None:
#         list_of_schedules = self.schedule
#         for schedule in list_of_schedules:
#             print("Start: " + schedule.hour_in + " End: " + schedule.hour_out)

class Employer:
    def __init__(self, name, id_num):
        self.name = name
        self.id = id_num
        self.crew = {}
        self.schedule = {}

    def new_employee(self):
        first = input('Enter: employee\'s first name:')
        last = input('Enter employees\'s last name: ')
        id_code = input('Enter id number: ')
        address = input('Enter address (street, city, state): ')
        phone = input('Enter phone number: ')
        email = input('Enter email: ')
        position = input('Enter position: ')
        # key = '{}.{}'.format(first.lower(), last.lower())
        new = {id_code: {'name': '{} {}'.format(first, last),
                         'id': id_code,
                         'contact': {'address': address,
                                     'phone': phone,
                                     'email': email},
                         'position': position}}
        return new

    def add_employee(self, n):
        # n is number of employees to add
        for i in range(n):
            contact = self.new_employee()
            self.crew.update(contact)

    def view_employee(self, key):
        return self.crew[key]

    def view_contact_info(self, key):
        print('Employee: {}'.format(self.crew[key]['name']))
        return self.crew[key]['contact']

    def weekly_schedule(self):
        for key in self.crew:
            temp = {self.crew[key]['id']: {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [],
                                           'Friday': [], 'Saturday': [], 'Sunday': []}}
            self.schedule.update(temp)
        return self.schedule

    def schedule_shift(self):
        empl_id = input('Enter ID of employee you want to schedule?: ')
        day = input('Which day did you want to schedule?: ').capitalize()
        start = format_time(input('Enter time-in: ').lower())
        end = format_time(input('Enter time-out: ').lower())
        self.schedule[empl_id][day].append([start, end])

    def view_employee_week(self, key):
        return self.schedule[key]

    # def update_contact(self):
    #     name = input('Enter employees username (Ex.first.last) ').lower()
    #     choice = input('What info needs to be updated?\n'
    #                       '1) Name\n'
    #                       '2) Contact Info\n'
    #                       '3) Position\n')
    #     if choice == '1':
    #         to_update = 'name'
    #         self.crew[name][to_update] = input('Enter new name: ')
    #     elif choice == '2':
    #         c = input('Which contact info needs to be changed?\n'
    #                   '1) Address\n'
    #                   '2) Phone Number\n'
    #                   '3) E-mail')
    #         if


def format_time(string):
    while True:
        string = string.replace(' ', '')
        if string[-1] != 'm':
            string += 'm'
        if string[-2] != 'a' and string[-2] != 'p':
            x = input('AM or PM ').lower()
            if 'a' in x:
                string = string.replace('m', 'am')
            elif 'p' in x:
                string = string.replace('m', 'pm')
        if int(string[0]) > 1 and len(string) < 7:
            string = '0' + string
        if int(string[3]) > 5 or string[2] != ':':
            string = input('Time entry invalid.\nEnter Time:')
        else:
            break
    return string


if __name__ == '__main__':
    boss = Employer('chris', '0001')
    boss.add_employee(1)
    boss.weekly_schedule()
    boss.schedule_shift()
    print(boss.schedule)








