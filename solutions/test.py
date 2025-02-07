import unittest
from flask import json
from src.app import app

class UnitTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello_endpoint(self):
        response = self.app.get("/") # This is to help you get started
        # TODO : Write a test for the '/' endpoint
        # TODO : Assert the status code is 200 
        # TODO : Assert the response is "Welcome to the Blueprint Software Dev Crash Course!"
    
    def test_get_tasks(self):
        # TODO : Write a test for the '/tasks' endpoint
        # TODO : Assert the status code is 200
        # TODO : Assert the response is a list
        # TODO : Assert the list is not empty
        # TODO : Assert the list contains a dictionary with keys "id", "title", and "completed"

if __name__ == "__main__":
    unittest.main()