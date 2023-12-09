from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def load_model(self):
        pass