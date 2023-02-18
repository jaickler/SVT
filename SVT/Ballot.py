# Defines the ballot class to digest and store voter choices.

from SVT.Candidate import Candidate

class Ballot():

    def __init__(self, scores: list[int]):
        '''Constructor to set initial variables for a ballot instance.\n
        scores contains the score for each candidate which should be stored at the same index as the candidate in the Election instance.\n
        ballot_id should be the unique index of this ballot in the election instance.'''
        self.candidates_scores:list[int] = scores
        self.id:int = 0
