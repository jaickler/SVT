# Import Unit Test & Candidate Class
import unittest
from SVT.Election import Election, Result
from SVT.Candidate import Candidate
from SVT.Ballot import Ballot
import sys
import os
import random
import inspect

# Used to fix path issues
sys.path.append(os.getcwd())

class TestBulkElection(unittest.TestCase):
    def test_bulk_random(self):
        ''' Test a set of random ballots for a 10 candidate election. '''

        # Initializes test election
        election_name = "Test Election"
        test_election = Election(election_name)

        # Creates 10 random candidates
        first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Isabella", "Jack"]
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        foods = ["pizza", "sushi", "pasta", "burger", "tacos", "ramen", "steak", "salad", "curry", "seafood"]

        for i in range(10):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"
            favorite_food = random.choice(foods)
            statement = f"My favorite food is {favorite_food}!"
            person = {"name": full_name, "statement": statement}
            test_election.add_candidate(Candidate(person["name"], person["statement"], "https://github.com/jaickler/SVT"))

        for i in range(0, 1000):
            temp_score:list[int] = []
            for j in range(0,10):
                temp_score.append(random.randint(0,5))
            test_election.cast_ballot(Ballot(temp_score))

        test_result = test_election.tally_votes()

        self.assertTrue(inspect.isclass(type(test_result)))


if __name__ == '__main__':
    unittest.main()