'''
Topic - Classes and Objects

class Developer:
  
    name: str
    salary: float
    language: str

    def code(self, text):
        return text

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

developer = Developer("Ed", 23000, "Python")
print(developer.code("Hello"))
'''
