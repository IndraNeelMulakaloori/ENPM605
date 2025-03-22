from space_robotics.models.robot.SpaceRobot import SpaceRobot

class PlanetaryRover(SpaceRobot):
    def __init__(self, name:str, sensor_system:object, mobility:str,terrain_type:str):
        super().__init__(name, sensor_system, mobility)
        self._terrain_type = terrain_type
        
    def move(self):
        return f"Moving: Using {self._mobility} across {self._terrain_type} terrain"
    
    def perform_task(self,task : str):
        
        task_str = f"\n-Robot: {self._name}"
        
        if task.lower() == 'mapping':
            return task_str + f"\n    {self.move()}\n{self._sensor_system.operate_sensors()}"
        
        elif task.lower() == 'collection':
            return task_str + f"\n    {self.move()}"
        
        return task_str + f"\n    Unsupported Task: {task}!!!!. Planetary Rover could only perform Mapping and Collection Tasks\n"
            
        
        
        
    