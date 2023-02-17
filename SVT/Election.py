# Defines the Election class that will be used to keep, run, and track a single election.
from SVT.Candidate import Candidate
from SVT.Ballot import Ballot
from typing import List

class Election:

    title:str = ""
    candidates:list[Candidate] = []
    ballots:list[Ballot] = []

    def __init__(self, election_name):
        ''' Constructor to set starting values of election. '''
        self.title = election_name

    def add_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)

    def cast_ballot(self, ballot: Ballot):
        '''Adds the proper score to each candidate in the election.\n
        Then sets the ballot id and adds it to the ballots list.'''

        # Iterates through each candidate and adds the score drom the ballot to that candidate.
        for item in range(0,len(self.candidates)):
            self.candidates[item].score += ballot.candidates_scores[item]

        # Sets ballot ID to its new index.
        ballot.id = len(self.ballots)

        # Adds ballot to the ballots list
        self.ballots.append(ballot)