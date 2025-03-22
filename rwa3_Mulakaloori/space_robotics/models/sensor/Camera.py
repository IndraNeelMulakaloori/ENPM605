from space_robotics.models.sensor.Sensor import Sensor

class Camera(Sensor):
    
    def __init__(self,model:str, range:float, pixel_resolution: int) -> None:
        super().__init__(model,range)
        self._pixel_resolution = pixel_resolution
        
    def get_info(self) -> str:
        return f"    Camera (Model : {self._model}, Range: {self._range}m Pixel Resolution : {self._pixel_resolution}MP)"
    
    def operate(self) -> str:
        return f"    {self._model} (Camera) Operation: Capturing Image at {self._pixel_resolution} resolution\n"
    