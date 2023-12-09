from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def load_dataset(self):
        pass