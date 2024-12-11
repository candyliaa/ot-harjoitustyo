import unittest
from ui.stats import Stats

class MockIO():
    def __init__(self, inputs):
        self.inputs = inputs

    def read(self, input_str):
        return self.inputs.pop(0)
    
    def print(self, input_str):
        pass
        

class TestStats(unittest.TestCase):
    def setUp(self):
        self.config = Config()
