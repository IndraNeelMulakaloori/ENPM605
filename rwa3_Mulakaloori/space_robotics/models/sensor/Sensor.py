from abc import ABC,abstractmethod


class Sensor(ABC):
    def __init__(self,model : str,range : float) -> None:
        self._model = model
        self._range = range
    
    @abstractmethod
    def get_info(self):
        pass
    
    @abstractmethod
    def operate(self):
        pass
