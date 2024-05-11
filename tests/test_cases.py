import unittest
from selenium import webdriver
from features.step_definitions.test_steps import *


class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        behave_runner = behave.runner.Runner()
        behave_runner.run_path("features/test.feature")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()