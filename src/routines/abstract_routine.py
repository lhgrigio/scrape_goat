from abc import ABC, abstractmethod

class AbstractRoutine(ABC):
    @abstractmethod
    def execute(self):
        pass