from abc import ABC,abstractmethod

class SpaceRobot(ABC):
    
    def __init__(self, name : str, sensor_system: object, mobility : str):
        self._name = name
        self._sensor_system = sensor_system
        self._mobility = mobility
    
    def activate(self):
        self._sensor_system.activate()
    
    @abstractmethod
    def perform_task(task):
        pass
        