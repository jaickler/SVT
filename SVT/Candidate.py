# Defines the Candidate class that will be used to keep the data for a single candidate.

class Candidate:

    def __init__(self, candidate_name, candidate_statement, candidate_url):
        ''' Constructor to set initial values for a candidate object '''

        self.id:int = 0
        self.name = candidate_name
        self.statement = candidate_statement
        self.url = candidate_url
        self.score:int = 0
