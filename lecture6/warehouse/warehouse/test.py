class TestAttribute:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def method1(self):
        self.z = 3

    def method2(self):
        print(self.z)

if __name__ == "__main__":
    test = TestAttribute(1, 2)
    test.method1()
    test.method2()