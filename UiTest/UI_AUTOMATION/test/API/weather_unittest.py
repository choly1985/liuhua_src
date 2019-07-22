import unittest
import requests
from urllib import parse
from time import sleep

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url = "fgfh"