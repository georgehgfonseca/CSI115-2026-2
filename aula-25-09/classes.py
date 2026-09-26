class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_approved(self):
        # ou apenas: return self.grade >= 6
        if self.grade >= 6:
            return True
        
        return False

    def __str__(self):
        return f"Student - name: {self.name} / grade: {self.grade} "


s1 = Student("Alice", 10)
s2 = Student("Bob", 5)
print(s1)
print(s2)