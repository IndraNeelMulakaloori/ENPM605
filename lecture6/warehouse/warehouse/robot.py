class Robot(object):
    # sensors = ["lidar", "camera", "radar"]

    def __init__(self, robot_id: str, model: str, battery_charge_level: float) -> None:
        self.robot_id = robot_id
        self.model = model
        self.battery_charge_level = battery_charge_level

    def move(self, destination: str, time_required) -> None:
        if self.battery_charge_level >= time_required:
            print(f"{self.model} Robot {self.robot_id} is moving to {destination}")
        else:
            print(
                f"{self.model} Robot {self.robot_id} has insufficient battery to move!"
            )

    # def __str__(self):
    #     return (
    #         f"Robot ID: {self.robot_id}\n"
    #         f"Model: {self.model}\n"
    #         f"Battery Charge Level: {self.battery_charge_level:.2f}\n"
    #         f"Sensors: {', '.join(self.sensors)}"
    #     )

    # def __call__(self, task: str) -> None:
    #     """Allows the robot to be 'called' like a function to perform a task."""
    #     print(f"Robot {self.robot_id} is executing task: {task}")

    # def __gt__(self, other):
    #     if isinstance(other, Robot):
    #         return self.battery_charge_level > other.battery_charge_level
    #     else:
    #         raise TypeError("Unsupported operand types for >")




if __name__ == "__main__":
    titan = Robot(robot_id="TN-8800", model="Titan", battery_charge_level=100.0)
    titan.move("store room", 2)

    nomad = Robot(robot_id="NMD-427", model="Nomad", battery_charge_level=50.0)
    nomad.move("loading dock", 1)

    # print(titan > nomad)
    # print(nomad)
    # nomad("loading dock")

    # print(nomad.sensors)
    # print(Robot.sensors)
    # print(Robot.robot_id)

    # test = TestAttribute(1, 2)
    # test.method1()
    # test.method2()
