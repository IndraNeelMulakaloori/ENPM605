from space_robotics.models.sensor.Sensor import Sensor


class LiDAR(Sensor):
    
    def __init__(self, model : str, range : float, angular_resolution : float) -> None:
        super().__init__(model, range)
        self._angular_resolution = angular_resolution
    
    def get_info(self) -> str:
        return f"LiDAR (Model : {self._model}, Range: {self._range}m, Angular_Resolution : {self._angular_resolution}°)"
    
    def operate(self) -> str:
        return f"\t{self._model} (LiDAR) Operation: Scanning terrain with {self._angular_resolution} resolution.\n"
    