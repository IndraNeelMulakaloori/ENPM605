from abc import ABC,abstractmethod
from space_robotics.models.sensor.SensorSystem import SensorSystem
#TODO : @property and aggregation/composition
class SpaceRobot(ABC):
    
    def __init__(self, name : str, sensor_system: dict[list], mobility : str):
        if not isinstance(sensor_system, dict):
            raise TypeError(f"Invalid Sensor System: {sensor_system}.")
        
        self._sensor_system = SensorSystem(sensor_system)
        self._name = name
        self._mobility = mobility
        
    ## Getters
    @property
    def name(self) -> str:
        return self._name
    
    @property 
    def sensor_system(self) -> SensorSystem:
        return self._sensor_system
    
    @property
    def mobility(self) -> str:
        return self._mobility
    
    ## Setters
    @name.setter
    def name(self,name : str) -> None:
        self._name = name
    
    @sensor_system.setter
    def sensor_system(self,sensor_system) -> None:
        if not isinstance(sensor_system, dict):
            raise TypeError(f"Invalid Sensor System : {sensor_system}.")
        self._sensor_system = SensorSystem(sensor_system)
    
    @mobility.setter
    def mobility(self,mobility : str) -> None:
        self._mobility = mobility
    
    
    
    def activate(self) :
        self.sensor_system.activate()
    
    @abstractmethod
    def perform_task(task : str):
        pass
        