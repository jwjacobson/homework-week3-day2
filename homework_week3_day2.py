#!/usr/bin/python

class Employee:
    raise_factor = 1.05

    def __init__(self, first_name, last_name, title, salary, email):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
        self.email = email
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.title} {self.salary} {self.email}"

    def employee_raise(self):
        self.salary *= self.raise_factor
        print(f"{self.first_name.title()} {self.last_name.title()} got a raise.")
        print(f"Their new salary is {self.salary}.")

employee1 = Employee("roy", "bland", "head of iron curtain networks", 30000, "none")
employee1.employee_raise()



