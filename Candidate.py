# Defines the Candidate class that will be used to keep the data for a single candidate.

class Candidate:
    
    id = 0
    name = ""
    statement = ""
    url = ""
    score = 0

    def __init__(self, id_number, candidate_name, candidate_statement, candidate_url) -> None:
        ''' Constructor to set initial values for a candidate object '''

        self.id = id_number
        self.name = candidate_name
        self.statement = candidate_statement
        self.url = candidate_url
