import unittest
from unittest.mock import Mock
import Twitter # name of my twitter program that needs to be tested.


class TwitterTest(unittest.TestCase):
    def test_example(self):
        self.mock_twitter = Mock()
        Twitter.tweet(mock_twitter, "message")
        mock_twitter.PostUpdate.assert_called_with("message")

    def test_example_punctuation(self):
        mock_twitter = Mock()
        Twitter.tweet(mock_twitter, "message!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        mock_twitter.PostUpdate.assert_called_with("message")

def main(): 
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(TwitterTest)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)

main()


