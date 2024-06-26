from main import Jenkins
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.x = 10
        self.y = 5
        self.jenkins = Jenkins(self.x, self.y)

    def test_addition(self):
        self.assertEqual(self.jenkins.add(), 15)
        
    def test_subtraction(self):
        self.assertEqual(self.jenkins.subtract(), 5)
        
    def test_multiply(self):
        self.assertEqual(self.jenkins.multiply(), 50)
        
    def test_division(self):
        self.assertEqual(self.jenkins.devide(), 2)


# if __name__ == "__main__":
#     main()
