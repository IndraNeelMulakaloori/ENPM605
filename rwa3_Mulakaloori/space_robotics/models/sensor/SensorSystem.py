from space_robotics.models.sensor.LiDAR import LiDAR
from space_robotics.models.sensor.Camera import Camera
from space_robotics.models.decorator import decorator
#TODO : @property and aggregation/composition
class SensorSystem():
    def __init__(self, sensors_map : dict[list]) -> None:
        self._status = 'inactive'
        
        if not isinstance(sensors_map,dict):
            raise TypeError("Invalid Sensor map. Pass Dict-list mapping as sensor_type : [attributes] pair")
        
        sensors_list = []
        for sensor_type, attributes in sensors_map.items():
            if sensor_type.lower() == 'lidar':
                sensors_list.append(LiDAR(attributes[0],attributes[1],attributes[2]))
            elif sensor_type.lower() == 'camera':
                sensors_list.append(Camera(attributes[0],attributes[1],attributes[2]))
            else :
                raise ValueError(f"Invalid Sensor Type : {sensor_type}. Valid sensor types are LiDAR and Camera")
                
        self._sensors = sensors_list
    @property
    def status(self) -> str:
        return self._status
    
    @property
    def sensors(self) -> list:
        return self._sensors
    
    @status.setter
    def status(self,status : str) -> None:
        self._status = status
        
    @sensors.setter
    def sensors(self,sensors : list) -> AttributeError:
        raise AttributeError("Modifying the sensors is not allowed.")
    
    #TODO: Contorl flow stop or continue
    @decorator
    def activate(self) -> str:
        if self.status == 'active':
            return f"Sensor System is already active.!!!!"
        
        self.status = 'active'
        
        activate_outputs = ""
        for sensor in self.sensors:
            activate_outputs += sensor.get_info() + "\n"
            
        return activate_outputs
    
    def operate_sensors(self) -> str:
        if self.status == 'inactive':
            return f"Sensor System is inactive. Activate the sensors first!!!!!!"
        
        operate_outputs = ""
        for sensor in self.sensors:
            operate_outputs += sensor.operate()
            
        return operate_outputs
    
        
    
        