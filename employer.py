from employee import Employee


class Employer:
    wage_dict = {0: 11.25, 1: 12.50, 2: 15.50, 3: 14.75, 4: 13.25}
    def __init__(self, name, id, contactinfo):
        self.name = name
        self.id = id
        self.contactinfo = contactinfo
        self.wage = wage_dict[2]

    def setwage(self, wage=11.25):
        if len(str(wage)) == 1 and wage in wage_dict.keys():
            emp_wage = wage
            return emp_wage
        elif len(str(wage)) == 5:
            for code, hourly in wage_dict.items():
                if wage == hourly:
                    emp_wage = code
                    return emp_wage


def gen_id():
    last_id = id_list.pop()
    new_id = last_id + 1
    id_list.append(last_id)
    id_list.append(new_id)
    return new_id


wage_dict = {0: 11.25, 1: 12.50, 2: 15.50, 3: 14.75, 4: 13.25}
emp_list = []
id_list = [0]

if __name__ == '__main__':
    TestEmployer = Employer('Darryl', gen_id(), "3322 SE 53rd Avenue")
    print(TestEmployer.name, TestEmployer.id, TestEmployer.contactinfo, TestEmployer.wage)
    TestEmp = Employee('Sullivan', gen_id(), 4)
    print(TestEmp.name, TestEmp.id, TestEmp.wage)
    print(TestEmp.set_wage(TestEmployer.setwage()))

# my gosh everything in here seems to work