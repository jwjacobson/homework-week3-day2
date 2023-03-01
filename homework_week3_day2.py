#!/usr/bin/python

# Exercise 1a
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

# Exercise 1b
class Sales(Employee):
    def __init__(self, first_name, last_name, title, salary, email, phone_number):
        super().__init__(first_name, last_name, title, salary, email)
        self.phone_number = phone_number

    def followup_email(self, customer_name):
        print(f"Dear {customer_name.title()}, Thank you for reaching out. My associates will be in touch shortly.")
        print(f"In the meantime, you can contact me by phone at {self.phone_number} or by email at {self.email}.")

class Development(Employee):
    def __init__(self, first_name, last_name, title, salary, email):
        super().__init__(first_name, last_name, title, salary, email)

    def code(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is writing code.")

# Exercise 1c
employee1 = Sales("wilfred", "sinecure", "head of customer relations", 50000, "wsinecure@org.org", "(123) 456 7890")
employee1.followup_email("Mike O'Neill")
employee1.followup_email("Hannah Stern")
employee1.employee_raise()

# Exercise 1d
employee2 = Development("monica", "tulayev", "sr. engineer", 100000, "mtulayev@org.org")
employee2.code()
employee2.employee_raise()


# Exercise 2
import geometry

print(geometry.area_of_circle(7))
print(geometry.hypotenuse(3, 4))