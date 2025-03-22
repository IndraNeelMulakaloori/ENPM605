from space_robotics.models.robot.SpaceRobot import SpaceRobot

class OrbitalRobotRover(SpaceRobot):
    def __init__(self, name:str, sensor_system:object, mobility:str,orbit_altitude:float):
        super().__init__(name, sensor_system, mobility)
        self._orbit_altitude = orbit_altitude
    
    def move(self):
        return f"Orbiting: Using {self._mobility} across {self._orbit_altitude}km terrain"
    
    def perform_task(self,task):
        task_str = f"\n-Robot: {self._name}"
        
        if task.lower() == 'repair':
            return task_str + f"    \n{self.move()}\n    Repairing: Satellite\n"
        
        elif task.lower() == 'maintenance':
            return task_str + f"    \n{self.move()}\n    Inspecting: Station hull\n"
        
        return task_str + f"\n   Unsupported Task: {task}!!!!. Orbital Robot Rover could only perform Repair and Maintenance Tasks\n"