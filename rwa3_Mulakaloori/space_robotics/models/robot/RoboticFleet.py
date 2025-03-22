from space_robotics.models.robot.SpaceRobot import SpaceRobot

class RoboticFleet():
    
    def __init__(self, robots : list[SpaceRobot]):
        self._robots = robots
    
    def add_robot(self,robot:SpaceRobot) -> str:
        confirmation_str = ""
        if isinstance(robot,SpaceRobot):
            self._robots.append(robot)
            confirmation_str = f"Added {robot._name} to fleet"
        else:
            confirmation_str = "Not a Space Robot. Couldn't Add to the fleet. Skipping!!!"
        
        return confirmation_str
    
    def remove_robot(self,robot:SpaceRobot) -> str:
        confirmation_str = ""
        
        if robot in self._robots:
            self._robots.remove(robot)
            confirmation_str = f"Removed {robot._name} from fleet"
        else :
            confirmation_str = f"{robot._name} is not in the fleet. Please try another Robot to remove"
        
        return confirmation_str
    
    def deploy_mission(self,task: str) -> str:
        
        combined_tasks = ""
        
        for robot in self._robots:
            combined_tasks += robot.perform_task(task)
        
        return combined_tasks
    
    def report_status(self):
        
        complete_robots_status = ""
        
        for robot in self._robots:
            complete_robots_status += f"-Robot: {robot._name}, Mobility: {robot._mobility}\n"
        
        return complete_robots_status
        
            

        
            
        