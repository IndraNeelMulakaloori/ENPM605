from space_robotics.models.sensor.Sensor import Sensor
#TODO : @property and aggregation/composition
class Camera(Sensor):
    
    def __init__(self,model:str, range: float, pixel_resolution: int) -> None:
        super().__init__(model,range)
        if not isinstance(pixel_resolution,int):
            raise TypeError("Invalid Data type. Pixel resolution must be an int.")
        self._pixel_resolution = pixel_resolution
    
    @property
    def pixel_resolution(self) -> int:
        return self._pixel_resolution
    
    @pixel_resolution.setter
    def pixel_resolution(self,pixel_resolution : int) -> None:
        if not isinstance(pixel_resolution,int):
            raise TypeError("Invalid Data type. Pixel resolution must be an int.")
        self._pixel_resolution = pixel_resolution
        
    def get_info(self) -> str:
        return f"        Camera (Model : {self.model}, Range: {self.range}m, Pixel Resolution : {self.pixel_resolution}MP)"
    
    def operate(self) -> str:
        return f"           {self.model} (Camera) Operation: Capturing Image at {self.pixel_resolution} resolution\n"
    