# Import Unit Test & Candidate Class
import unittest
from SVT.Candidate import Candidate
import sys
import os

# Used to fix path issues
sys.path.append(os.getcwd())

class TestCandidate(unittest.TestCase):
    def test_construction_variable_id(self):
        """
        Test that the Constructor function can properly set id variables.
        """
        
        # Sets test values for class variables.
        id_number = 115
        candidate_name = "Dr. Richtofen"
        candidate_statement = "My lucky number is 115."
        candidate_url = "https://github.com/jaickler/SVT"

        # Creates test Candidate object
        test_candidate = Candidate(id_number, candidate_name, candidate_statement, candidate_url)

        # Checks to make sure id_number was set properly
        self.assertEqual(test_candidate.id, id_number)

    def test_construction_variable_name(self):
        """
        Test that the Constructor function can properly set name variables.
        """
        
        # Sets test values for class variables.
        id_number = 115
        candidate_name = "Dr. Richtofen"
        candidate_statement = "My lucky number is 115."
        candidate_url = "https://github.com/jaickler/SVT"

        # Creates test Candidate object
        test_candidate = Candidate(id_number, candidate_name, candidate_statement, candidate_url)

        # Checks to make sure id_number was set properly
        self.assertEqual(test_candidate.name, candidate_name)

    def test_construction_variable_statement(self):
        """
        Test that the Constructor function can properly set statement variables.
        """
        
        # Sets test values for class variables.
        id_number = 115
        candidate_name = "Dr. Richtofen"
        candidate_statement = "My lucky number is 115."
        candidate_url = "https://github.com/jaickler/SVT"

        # Creates test Candidate object
        test_candidate = Candidate(id_number, candidate_name, candidate_statement, candidate_url)

        # Checks to make sure id_number was set properly
        self.assertEqual(test_candidate.statement, candidate_statement)

    def test_construction_variable_url(self):
        """
        Test that the Constructor function can properly set url variables.
        """
        
        # Sets test values for class variables.
        id_number = 115
        candidate_name = "Dr. Richtofen"
        candidate_statement = "My lucky number is 115."
        candidate_url = "https://github.com/jaickler/SVT"

        # Creates test Candidate object
        test_candidate = Candidate(id_number, candidate_name, candidate_statement, candidate_url)

        # Checks to make sure id_number was set properly
        self.assertEqual(test_candidate.url, candidate_url)

if __name__ == '__main__':
    unittest.main()