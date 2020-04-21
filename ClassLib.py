class Employee:
    """A sample Employee class"""

    def __init__(self, employee_id, first, last, job, pay1, dpto1):
        self.employee_id=employee_id
        self.first = first
        self.last = last
        self.job = job
        self.pay = pay1
        self.dpto = dpto1

class Department:
    """A sample Department class"""

    def __init__(self, name, budget, phone):
        self.name = name
        self.budget = budget
        self.phone = phone

class PaymentHistory:
    """A sample Transaction class"""

    def __init__(self, employee, netpay, dates):
        self.employee = employee
        self.netpay = netpay
        self.dates = dates
        
    