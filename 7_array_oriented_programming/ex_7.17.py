# ex_7.17
import numpy as np

votes = np.random.randint(0, 2, size=99 )

vote_counts = np.bincount(votes)

# Display the results
print( "votes array: " )
print( votes )
print( "\nVote counts:" )
print( f"Candidate 1 (0's): {vote_counts[0]}")
print( f"Candidate 2 (1's): {vote_counts[1]}")