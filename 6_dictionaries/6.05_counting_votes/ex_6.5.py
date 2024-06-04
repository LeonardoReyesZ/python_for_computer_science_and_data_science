""" script that uses a dictionary to determine the number of votes received by a candidate.
    The votes are concatenated in a string """

# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# function to count the votes and return them in a dictionary
def count_votes( vote_string ):
    # split the vote string by commas to get a list of votes
    votes = vote_string.split(',')

    # initialize an empty dictionary to count votes for each candidate
    vote_count = {}

    # iterate through the list of votes
    for vote in votes:
        # strip any whitespace around the vote
        candidate = vote.strip()

        # if the candidate is already in the dictionary, increment their count
        if candidate in vote_count:
            vote_count[candidate] += 1
        # if the candidate is not in the dictionary, add them with a count of 1
        else:
            vote_count[candidate] = 1

    return vote_count
# end function count_votes


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
vote_string = "Alice, Bob, Alice, Charlie, Bob, Alice, Bob, Charlie, Charlie, Bob, Alice"
result = count_votes(vote_string)

# print the results
for candidate, count in result.items():
    print(f"{candidate}: {count} votes")
