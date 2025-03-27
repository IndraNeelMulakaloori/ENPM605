from space_robotics.models.robot.SpaceRobot import SpaceRobot
from space_robotics.models.decorator import decorator
#TODO : @property and aggregation/composition
class RoboticFleet():
    def __init__(self):
        self._robots = []
    
    @property
    def robots(self):
        return self._robots
    
    @robots.setter
    def robots(self, robots : list[SpaceRobot]):
        self._robots = robots
    
    @decorator
    def add_robot(self,robot:SpaceRobot) -> str:
        confirmation_str = ""
        if isinstance(robot,SpaceRobot):
            self.robots.append(robot)
            confirmation_str = f"       -Added {robot.name} to fleet\n"
        else:
            confirmation_str = f"       -{robot} Not a Space Robot. Couldn't Add to the fleet. Skipping!!!\n"
        
        return confirmation_str
    
    @decorator
    def remove_robot(self,robot:SpaceRobot) -> str:
        confirmation_str = ""
        
        if robot in self._robots:
            self.robots.remove(robot)
            confirmation_str = f"       -Removed {robot.name} from fleet\n"
        else :
            confirmation_str = f"       -{robot.name} is not in the fleet. Please try another Robot to remove\n"
        
        return confirmation_str
    
    @decorator
    def deploy_mission(self,task: str) -> str:
        
        combined_tasks = ""
        
        for robot in self.robots:
            combined_tasks += robot.perform_task(task)
        
        return combined_tasks
    
    @decorator
    def report_status(self):
        
        complete_robots_status = ""
        
        for robot in self.robots:
            complete_robots_status += f"       -Robot: {robot.name}, Mobility: {robot.mobility}\n"
        
        return complete_robots_status
        
            

        
            
        