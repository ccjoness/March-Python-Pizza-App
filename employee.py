# Driver list presumably already returned from method donald is building.
# Same as above in regards to order list.


# so I need to tell donald I would like an available_driver_list and current_order_list
# tell donald about my plans for a dispatch_dict


class Employee:
    def __init__(self, name, emp_id, wage_code=0):
        self.name = name
        self.id = emp_id
        self.wage = wage_dict[wage_code]

    def dispatch(self, driver_id, order_id):
        # signify in some way that the driver is now busy - change attribute if class or something
        # maybe return key:value pair of driver and current order?
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
    order_list = []  # this should be retur
    driver_list = []  # this should be returned to me from donald's method
    wage_dict = {0: 11.25, 1: 12.50, 2: 15.50, 3: 14.75, 4: 13.25, 5: 25.25}  # not sure where to naturally integrate
    dispatch_dict = {}
    TestEmp = Employee('Sullivan', gen_id())
    TestEmp.setwage(1)
    print(TestEmp.name, TestEmp.id, TestEmp.wage)
