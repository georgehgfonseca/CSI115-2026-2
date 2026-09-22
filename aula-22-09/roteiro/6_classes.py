class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
print(s1.greet())
print(s2.greet())
print(s1)