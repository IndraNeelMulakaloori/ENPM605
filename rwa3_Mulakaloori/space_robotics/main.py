"""
# Program Testing

In `main()`, implement the following code to test different aspects of your program:
  - Create a `PlanetaryRover` robot:
    - Name: `MarsExplorer`
    - Mobility: `wheels`
    - Terrain: `rocky`
    - Sensors:
      - LiDAR: `"X-500"`, `100.0`, `0.5`
      - LiDAR: `"OS1"`, `20.5`, `1.5`
      - Camera: `"CamPro"`, `50.0`, `20`
  - Create an `OrbitalRobotRover` robot:
    - Name: `OrbitFixer`
    - Mobility: `thrusters`
    - Altitude: `400.5`
    - Sensors:
      - LiDAR: `"X-500"`, `100.0`, `0.5`
      - Camera: `"CamPro"`, `50.0`, `20`
      - Camera: `"OrbitCam"`, `20.0`, `20`
  - Create a robotic fleet
  - Add both robots to the fleet
  - Report the status of the fleet
  - Activate the sensors for all robots in the fleet
  - Deploy mission `mapping`, `collection`, `repair`, and `maintenance`
  - Remove `OrbitalRobotRover` from the fleet
  - Deploy mission `maintenance` and `mapping`
  - Report the status of the fleet
  
Note: If I create a third robot and I add it to the fleet, your fleet operations should
still work (use for loop)
"""
import sys
import os.path

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path)


from space_robotics.models.sensor.LiDAR import LiDAR
from space_robotics.models.sensor.Camera import Camera
from space_robotics.models.sensor.SensorSystem import SensorSystem
from space_robotics.models.robot.PlanetaryRover import PlanetaryRover



def main():
    # new_lidar = LiDAR("X-500",100.0,0.5)
    # print(new_lidar.get_info())
    # print(new_lidar.operate())
    # new_camera = Camera("CamPro",50,12)
    # print(new_camera.get_info())
    # print(new_camera.operate())
    
    # # print(type(new_camera))
    # # print(isinstance(new_camera,Sensor))
    
    # sensor_system = SensorSystem([new_camera,new_lidar,"Data 1"])
    # print(sensor_system.activate())
    # print(sensor_system.operate_sensors())
    
    mars_rover = PlanetaryRover(
      "Mars Explorer",
      SensorSystem([
        LiDAR("X-500",100.0,0.5),
        LiDAR("OSI",20.5,1.5),
        Camera("CamPro",50,12)
      ]),
      "wheels",
      "rocky"
    )
    mars_rover.activate()
    # print(mars_rover.move())
    print(mars_rover.perform_task('collectio'))
    
if __name__ == '__main__':
    main()