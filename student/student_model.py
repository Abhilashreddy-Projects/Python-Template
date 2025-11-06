from person_model import Person

class Student(Person):
    def __init__(self, id: int, name: str, marks: dict, age: int):
        self.id= id
        self.marks=marks
        super().__init__(name, age)

