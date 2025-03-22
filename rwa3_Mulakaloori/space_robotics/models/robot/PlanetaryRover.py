from space_robotics.models.robot.SpaceRobot import SpaceRobot

class PlanetaryRover(SpaceRobot):
    def __init__(self, name:str, sensor_system:object, mobility:str,terrain_type:str):
        super().__init__(name, sensor_system, mobility)
        self._terrain_type = terrain_type
        
    def move(self):
        return f"\tMoving: Using {self._mobility} across {self._terrain_type} terrain\n"
    
    def perform_task(self,task : str):
        
        if task.lower() == 'mapping':
            return f"\n-Robot: {self._name}\n{self.move()}\n{self._sensor_system.operate_sensors()}"
        
        elif task.lower() == 'collection':
            return f"\n-Robot: {self._name}\n{self.move()}"
        
        return "\nInvalid task!!!!. Planetary Rover could only perform Mapping and Collection Tasks\n"
            
        
        
        
    