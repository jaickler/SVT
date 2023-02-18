# Import Unit Test & Candidate Class
import unittest
from SVT.Ballot import Ballot
import sys
import os

# Used to fix path issues
sys.path.append(os.getcwd())

class TestBallot(unittest.TestCase):

    def test_constructor_variable(self):
        '''Test that the constructor properly sets the candidate scores.'''
        test_ballot = Ballot([0,1,2,3,4,5])

        self.assertEqual(test_ballot.candidates_scores, [0,1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()