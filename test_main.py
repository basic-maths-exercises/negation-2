import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        source = inspect.getsource(negationBetween)
        self.assertTrue( source.find("if")!=-1, "Your negation function should contain an if statement" )
        self.assertTrue( numberBetween(data,1,9)==len(data) - negationBetween(data,1,9), "Your function for the negation is not returning the expected number" )
        self.assertTrue( numberBetween(data,2,7)==len(data) - negationBetween(data,2,7), "Your function for the negation is not returning the expected number" )
        self.assertTrue( numberBetween(data,4,6)==len(data) - negationBetween(data,4,6), "Your function for the negation is not returning the expected number" )
