# Defines the Election class that will be used to keep, run, and track a single election.
from Candidate import Candidate

class Election:

    title = ""
    candidates = []

    def __init__(self, election_name):
        ''' Constructor to set starting values of election. '''
        self.title = election_name

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    