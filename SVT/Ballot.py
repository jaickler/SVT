# Defines the ballot class to digest and store voter choices.

from Candidate import Candidate

class Ballot():

    # Used to store the scores for each candidate. Candidate scores are in the same index as the candidate's object in the Election instance.
    candidates_scores:list[int] = []
    # Unique sequential ID for specific ballot. Also the index of this ballot in the Election instance.
    id = 0

    def __init__(self, scores: list[int]):
        '''Constructor to set initial variables for a ballot instance.\n
        scores contains the score for each candidate which should be stored at the same index as the candidate in the Election instance.\n
        ballot_id should be the unique index of this ballot in the election instance.'''
        self.candidates_scores = scores
