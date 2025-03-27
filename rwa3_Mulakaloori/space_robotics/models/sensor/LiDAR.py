from space_robotics.models.sensor.Sensor import Sensor

#TODO : @property and aggregation/composition
class LiDAR(Sensor):
    
    def __init__(self, model : str, range : float, angular_resolution : float) -> None:
        super().__init__(model, range)
        if not isinstance(angular_resolution,float):
            raise TypeError("Invalid Data type. Angular resolution must be a floating point")
        self._angular_resolution = angular_resolution
    
    @property
    def angular_resolution(self) -> float:
        return self._angular_resolution
    
    @angular_resolution.setter
    def angular_resolution(self,angular_resolution : float) -> None:
        if not isinstance(angular_resolution,float):
            raise TypeError("Invalid Data type. Angular resolution must be a floating point")
        self._angular_resolution = angular_resolution
    
    
    def get_info(self) -> str:
        return f"        LiDAR (Model : {self.model}, Range: {self.range}m, Angular_Resolution : {self.angular_resolution}°)"
    
    def operate(self) -> str:
        return f"           {self.model} (LiDAR) Operation: Scanning terrain with {self.angular_resolution} resolution\n"
    