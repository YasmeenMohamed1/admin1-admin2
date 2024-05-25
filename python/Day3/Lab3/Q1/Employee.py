from Human import Human

class Employee(Human):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary=salary

    def Speak(self):
        print(f'I am {self.name} and my salary is {self.salary}')

    
    