from space_robotics.models.sensor.Sensor import Sensor


class SensorSystem():
    def __init__(self, sensors : list[Sensor]) -> None:
        self._sensors = sensors
        self._status = 'inactive'
    
    def activate(self) -> list:
        self._status = 'active'
        
        valid_sensor_info = []
        for sensor in self._sensors:
            if isinstance(sensor,Sensor):
                valid_sensor_info.append(sensor.get_info())
            else:
                valid_sensor_info.append(f"Invalid Sensor : {sensor}. No output")
        return valid_sensor_info
    
    def operate_sensors(self) -> str:
        operate_outputs = ""
        
        for sensor in self._sensors:
            if isinstance(sensor,Sensor):
                operate_outputs += sensor.operate()
            else:
                operate_outputs += f"Invalid Sensor : {sensor}. No output\n"
        
        return operate_outputs
        
    
        