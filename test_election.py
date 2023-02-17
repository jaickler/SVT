# Import Unit Test & Candidate Class
import unittest
from SVT.Election import Election
from SVT.Candidate import Candidate
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

    def test_add_candidate_empty(self):
        '''Test that the add_candidate function properly adds a candidate to an empty candidates list.'''
        election_name = "Test Election"
        test_election = Election(election_name)
        test_election.add_candidate(Candidate("Richtofen", "115 is my favorite number", "https://github.com/jaickler/SVT"))
        self.assertEqual(test_election.candidates[0].id, 0)

    def test_add_candidate_append(self):
        '''Test that the add_candidate function properly adds a candidate to an empty candidates list.'''
        election_name = "Test Election"
        test_election = Election(election_name)
        test_election.add_candidate(Candidate("Richtofen", "115 is my favorite number", "https://github.com/jaickler/SVT"))
        test_election.add_candidate(Candidate("Dempsey", "I hate the Dr.", "https://github.com/jaickler/SVT"))
        self.assertEqual(test_election.candidates[1].id, 1)


if __name__ == '__main__':
    unittest.main()