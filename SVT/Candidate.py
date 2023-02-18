# Defines the Candidate class that will be used to keep the data for a single candidate.

class Candidate:

    def __init__(self, candidate_name:str, candidate_statement:str, candidate_url:str):
        ''' Constructor to set initial values for a candidate object '''
        # Unique id of candidate is also the index of the Election.candidates list.
        self.id:int = 0

        # Candidate name.
        self.name:str = candidate_name

        # Brief statment from or about the candidate.
        self.statement:str = candidate_statement

        # URL for or about candidate. Can be left as blank string.
        self.url:str = candidate_url

        # Score of candidate calculated as ballots are cast.
        self.score:int = 0

        # Number of ballots won during runoff portion of election.
        self.ballots:int = 0

        # Defaults the candidate to be part of the election.
        self.disqualified:bool = False
