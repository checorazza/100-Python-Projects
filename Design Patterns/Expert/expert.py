from abc import ABC, abstractmethod

class OrderProcessingExpert(ABC):
    @abstractmethod
    def process(self, order):
        pass
