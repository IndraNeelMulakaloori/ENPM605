from space_robotics.models.robot.SpaceRobot import SpaceRobot
#TODO : @property and aggregation/composition
class PlanetaryRover(SpaceRobot):
    def __init__(self, name:str, sensor_system: dict[list], mobility:str,terrain_type:str):
        super().__init__(name, sensor_system, mobility)
        self._terrain_type = terrain_type
    
    @property
    def terrain_type(self) -> str:
        return self._terrain_type
    
    @terrain_type.setter
    def terrain_type(self,terrain_type) -> None:
        self._terrain_type = terrain_type
        
    def move(self):
        return f"Moving: Using {self.mobility} across {self.terrain_type} terrain"
    
    def perform_task(self,task : str):
        
        task_str = f"       -Robot: {self.name}"
        
        if task.lower() == 'mapping':
            return task_str + f"\n           {self.move()}\n{self.sensor_system.operate_sensors()}"
        
        elif task.lower() == 'collection':
            return task_str + f"\n           {self.move()}\n"
        
        return task_str + f"\n           Unsupported Task: {task}!!!!. Planetary Rover could only perform Mapping and Collection Tasks\n"
            
        
        
        
    