from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self,name):
        self.name = name

    
    def Speak(self):
        pass