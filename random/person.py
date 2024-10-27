class Person:
    def __init__(self, name, age, dob=None):
        self.name = name
        self.age = age
        self.dob = dob

    def __str__(self):
        return f"{self.name} {self.age} {self.dob}"
