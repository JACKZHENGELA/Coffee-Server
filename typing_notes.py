class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

jack = Person(name="Jack", age=16)
print(jack)

def register_user(person:Person):
    print(person.name)

register_user(person=jack)