# Defines the Election class that will be used to keep, run, and track a single election.
from SVT.Candidate import Candidate
from SVT.Ballot import Ballot
from typing import List


class Result:
    ''' Used to house the results of an election. '''
    def __init__(self, win_or_tie:str, candidates:list[Candidate]) -> None:
        ''' Creates a Result object containing a string of "win" or "tie" and a list of Candidate objects. '''

        # Sets the result to "win" or "tie".
        self.result:str = win_or_tie

        # Sets the candidates list to be the winner or tied candidates.
        self.candidates:list[Candidate] = candidates

class Election:
    ''' Class used to track and run a STAR election in a self contained object. '''
    def __init__(self, election_name):
        ''' Constructor to set starting values of election. '''
        
        # Sets the title of the Election.
        self.title = election_name

        # Sets the list of candidates as an empty list.
        self.candidates:list[Candidate] = []

        # Sets the list of ballots as an empty list.
        self.ballots:list[Ballot] = []

    def add_candidate(self, candidate: Candidate):
        ''' Appends the candidate object to the candidates list for this election. '''

        # Sets the candidate's id to its index in the candidates list.
        candidate.id = len(self.candidates)

        # Adds candidate to candidates list.
        self.candidates.append(candidate)

    def disqualify_candidate(self, candidate_id:int):
        ''' Sets the disqualified attribute of a candidate to True, removing them from election results. '''
        self.candidates[candidate_id].disqualified = True

    def reinstate_candidate(self, candidate_id:int):
        ''' Sets the disqualified attribute of a candidate to False, allowing them to partake in the election. '''
        self.candidates[candidate_id].disqualified = False

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

    def tally_votes(self) -> Result:
        ''' Counts the votes and returns a Result'''

        # Sets disqualified candidates' scores to 0.
        for candidate in self.candidates:
            if candidate.disqualified == True:
                candidate.score = 0

        # Starts the Initial Score phase of the election by sorting the candidates by score
        self.candidates.sort(key = lambda x: x.score, reverse=True)


        # Tallies the ballots of the top two scoring candidates.
        for ballot in self.ballots:
            if ballot.candidates_scores[self.candidates[0].id] > ballot.candidates_scores[self.candidates[1].id]:
                self.candidates[0].ballots += 1
            elif ballot.candidates_scores[self.candidates[0].id] < ballot.candidates_scores[self.candidates[1].id]:
                self.candidates[1].ballots += 1
            else:
                continue
        
        # Determines the result of the election and returns a Result object.

        # Checks if the first candidate won.
        if self.candidates[0].ballots > self.candidates[1].ballots:
            return Result("win", [self.candidates[0]])  

        # Checks if the second candidate won.
        elif self.candidates[0].ballots < self.candidates[1].ballots:
            return Result("win", [self.candidates[1]])

        # Reports tie if neither candidate had a higher score. Both scores must be equal.
        else:
            return Result("tie", [self.candidates[0], self.candidates[1]])
