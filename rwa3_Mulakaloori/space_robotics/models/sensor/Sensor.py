from abc import ABC,abstractmethod

#TODO : @property and aggregation/composition
class Sensor(ABC):
    def __init__(self,model : str,range : float) -> None:
        if not isinstance(model,str) :
            raise TypeError("Invalid Data type. model must be a string")
        if not isinstance(range,float):
            raise TypeError("Invalid Data type. range must be a float ")
        self._model = model
        self._range = range
    
    @property
    def model(self) -> str:
        return self._model
    
    @property
    def range(self) -> float:
        return self._range
    
    
    @model.setter
    def model(self, model) -> AttributeError:
        raise AttributeError("Modifying the model is not allowed.")
    
    @range.setter
    def range(self,range : float) -> (TypeError | None):
        if not isinstance(range,float):
            raise TypeError("Invalid Data type. range must be a float ")
        self._range = range
        
    @abstractmethod
    def get_info(self):
        pass
    
    @abstractmethod
    def operate(self):
        pass
