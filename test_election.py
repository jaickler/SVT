# Import Unit Test & Candidate Class
import unittest
from SVT.Election import Election
import sys
import os

# Used to fix path issues
sys.path.append(os.getcwd())

class TestElection(unittest.TestCase):
    def test_construction_variable_title(self):
        '''Test that the Constructor function properly sets the title variable'''
        election_name = "Test Election"
        test_election = Election(election_name)
        self.assertEqual(test_election.title, election_name)

if __name__ == '__main__':
    unittest.main()