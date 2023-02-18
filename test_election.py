# Import Unit Test & Candidate Class
import unittest
from SVT.Election import Election, Result
from SVT.Candidate import Candidate
from SVT.Ballot import Ballot
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

    def test_cast_ballot_empty(self):
        ''' Test that the cast_ballot function properly places the first ballot in an election when given a valid ballot.'''
        election_name = "Test Election"
        test_election = Election(election_name)
        test_election.add_candidate(Candidate("Richtofen", "115 is my favorite number", "https://github.com/jaickler/SVT"))
        test_election.add_candidate(Candidate("Dempsey", "I hate the Dr.", "https://github.com/jaickler/SVT"))
        test_ballot = Ballot([1,5])
        test_election.cast_ballot(test_ballot)

        self.assertEqual(test_election.ballots[0].id, 0)

    def test_cast_ballot_append(self):
        ''' Test that the cast_ballot function properly places multiple ballots on the list properly.'''
        election_name = "Test Election"
        test_election = Election(election_name)
        test_election.add_candidate(Candidate("Richtofen", "115 is my favorite number", "https://github.com/jaickler/SVT"))
        test_election.add_candidate(Candidate("Dempsey", "I hate the Dr.", "https://github.com/jaickler/SVT"))

        for cast in range(0,5):
            test_ballot = Ballot([cast,5])
            test_election.cast_ballot(test_ballot)

        self.assertEqual(test_election.ballots[4].candidates_scores[0], 4)

    def test_tally_votes_win(self):
        ''' Test to see if the tally_votes function can properly report a winning result. '''

        # Sets up test election.
        election_name = "Test Election"
        test_election = Election(election_name)
        test_election.add_candidate(Candidate("Richtofen", "115 is my favorite number", "https://github.com/jaickler/SVT"))
        test_election.add_candidate(Candidate("Dempsey", "I hate the Dr.", "https://github.com/jaickler/SVT"))
        test_election.add_candidate(Candidate("Bob", "We can fix it.", "https://github.com/jaickler/SVT"))

        # Casts five ballots.
        for cast in range(0,5):
            test_ballot = Ballot([cast,5,0])
            test_election.cast_ballot(test_ballot)

        # Tallys the votes.
        test_result:Result = test_election.tally_votes()

        self.assertEqual(test_result.result+test_result.candidates[0].name, "winDempsey")

        
if __name__ == '__main__':
    unittest.main()