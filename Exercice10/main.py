# Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"{self.name} a {self.age} ans"


class Employee(Person):
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)

    def display_details(self):
        print(f"{super().display_details()} et son salaire est {self.salary}€")


employee = Employee("Anthony", 37, 2000)
employee.display_details()
