#MyProgram:Test code
import unittest # this is required for unit test
import MyProgram # program that need to be tested

class TestMyProgram(unittest.TestCase):
 # we write our test cases here
 # test_ will tell the program that it is test case method
 # python convention to name test cases.
    def test_square_int(self):
        # this will check if the resultant values are equal 
        # where first param is the expectedresult 
        # and the second param is the actual result.
        self.assertEqual(25,MyProgram.square(5))

    def test_cube_int(self):
        self.assertEqual(8,MyProgram.cube(2))

    def test_square_float(self):
        # the expected result should be equal to the actual result upto 2 decimal digits.
        self.assertAlmostEqual(3.72,MyProgram.square(1.93),2)

    def test_cube_float(self):
        self.assertAlmostEqual(10.503,MyProgram.cube(2.19),3)

# this is required for test suite and run it
def main(): 
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(TestMyProgram)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
main()