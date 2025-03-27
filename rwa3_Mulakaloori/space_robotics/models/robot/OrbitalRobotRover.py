from space_robotics.models.robot.SpaceRobot import SpaceRobot
#TODO : @property and aggregation/composition
class OrbitalRobotRover(SpaceRobot):
    def __init__(self, name:str, sensor_system:dict[list], mobility:str,orbit_altitude:float) -> None:
        super().__init__(name, sensor_system, mobility)
        if not isinstance(orbit_altitude,float):
            raise TypeError("Invalid Data Type. orbit_altitude must be a floating point")
        self._orbit_altitude = orbit_altitude
    
    @property
    def orbit_altitude(self) -> str:
        return self._orbit_altitude
    
    @orbit_altitude.setter
    def orbit_altitude(self, orbit_altitude) -> None:
         if not isinstance(orbit_altitude,float):
            raise TypeError("Invalid Data Type. orbit_altitude must be a floating point")
         self._orbit_altitude = orbit_altitude
    
    def move(self) -> str:
        return f"           Orbiting: Using {self.mobility} across {self.orbit_altitude}km terrain"
    
    def perform_task(self,task) -> str:
        task_str = f"       -Robot: {self.name}"
        
        if task.lower() == 'repair':
            return task_str + f"      \n{self.move()}\n           Repairing: Satellite\n"
        
        elif task.lower() == 'maintenance':
            return task_str + f"      \n{self.move()}\n           Inspecting: Station hull\n"
        
        return task_str + f"\n           Unsupported Task: {task}!!!!. Orbital Robot Rover could only perform Repair and Maintenance Tasks\n"