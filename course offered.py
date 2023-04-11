

class Course:
    def _init_(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
        
    def display_course(self):
        print(f"{self.code}: {self.name} ({self.credits} credits)")

class Elective(Course):
    def _init_(self, name, code, credits, prerequisites):
        super()._init_(name, code, credits)
        self.prerequisites = prerequisites
        
    def display_course(self):
        super().display_course()
        print(f"Prerequisites: {', '.join(self.prerequisites)}")

class Core(Course):
    def _init_(self, name, code, credits, required):
        super()._init_(name, code, credits)
        self.required = required
        
    def display_course(self):
        super().display_course()
        if self.required:
            print("This course is required.")
        else:
            print("This course is not required.")
courses = [
    Core("Introduction to Programming", "CS101", 4, True),
    Core("Data Structures and Algorithms", "CS201", 4, True),
    Elective("Computer Networks", "CS301", 4, ["CS201"]),
    Elective("Artificial Intelligence", "CS302", 4, ["CS201"]),
]

for course in courses:
    course.display_course()



