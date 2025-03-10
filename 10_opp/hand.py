#hand.py
"""Hand class that represents a five-card poker hand."""
from cardtotalordering import Card
from functools import total_ordering

@total_ordering
class Hand:
    def __init__(self, cards):
        """Initialize the hand with a list of 5 cards."""
        if len(cards) != 5:
            raise ValueError("A hand must contain 5 cards.")

        # FACES with a high 'ace' to evaluate highest card
        self.FACES_A = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.cards = sorted(cards) # in ascending order

    def evaluate(self):
        """Evaluate the strength of the hand and return a tuple(ranking and values)."""
        faces = [card.face for card in self.cards]
        suits = [card.suit for card in self.cards]
        face_counts = {face: faces.count(face) for face in faces}
        unique_faces = sorted(set(faces))

        is_flush = len(set(suits)) == 1
        is_straight = self._is_consecutive(faces)

        # check for  royal flush
        if is_flush and set(faces) == {'ace','10', 'jack', 'queen', 'king'}:
            return (9, unique_faces)

        # check for straight flush
        if is_flush and is_straight:
            return (8, unique_faces)

        # check for four of a kind
        if 4 in face_counts.values():
            return (7, unique_faces)

        # check for full house
        if 3 in face_counts.values() and 2 in face_counts.values():
            full_faces = {v: k for k, v in face_counts.items()}
            return (6, [full_faces.get(3), full_faces.get(2)]) # return by priority

        # check for flush
        if is_flush:
            return (5, unique_faces)

        # check for straight
        if is_straight:
            return (4, unique_faces)

        # check for three of a kind
        if 3 in face_counts.values():
            three_face = [k for k, v in face_counts.items() if v == 3]
            remaining_faces = [k for k, v in face_counts.items() if v!=3]

            sort_face = self.FACES_A.index(three_face[0])
            sort_remain = sorted([self.FACES_A.index(face) for face in remaining_faces], reverse=True)

            return_indexes = [sort_face] + [face for face in sort_remain]
            return (3, return_indexes)  # return (indexes) by priority

        # check for two pair
        if list(face_counts.values()).count(2) == 2:
            pair_faces = [k for k, v in face_counts.items() if v == 2]
            remaining_faces = [k for k,v in face_counts.items() if v != 2]

            sort_faces = sorted([self.FACES_A.index(face) for face in pair_faces], reverse=True)
            sort_remain = sorted([self.FACES_A.index(face) for face in remaining_faces], reverse=True)

            return_indexes = [face for face in sort_faces] + [face for face in sort_remain]
            return (2, return_indexes)

        # check for one pair
        if 2 in face_counts.values():
            pair_face = [k for k,v in face_counts.items() if v == 2]
            remaining_faces = [k for k,v in face_counts.items() if v != 2]

            sort_face = self.FACES_A.index(pair_face[0])
            sort_remain = sorted([self.FACES_A.index(face) for face in remaining_faces], reverse=True)

            return_indexes = [sort_face] + [face for face in sort_remain]
            return (1, return_indexes)

        # high card
        return (0, unique_faces)

    def _is_consecutive(self, faces):
        """Check if the faces form a consecutive sequence."""
        indices = sorted([Card.FACES.index(face) for face in faces])

        # check for a consecutive sequence
        return indices == list(range(min(indices), max(indices) + 1))

    def __eq__(self, other):
        """Return True if self == other."""
        if not isinstance(other, Hand):
            return NotImplemented

        return self.evaluate() == other.evaluate()

    def __lt__(self, other):
        """Return True if self < other."""
        if not isinstance(other, Hand):
            return NotImplemented

        self_rank, self_faces = self.evaluate()
        other_rank, other_faces = other.evaluate()

        if self_rank != other_rank:
            return self_rank < other_rank # return the best rank

        # find the best high cards
        if self_rank == 6: # exception to evaluate a full house
            self_sorted = [self.FACES_A.index(face) for face in self_faces]
            other_sorted = [self.FACES_A.index(face) for face in other_faces]

        # exception for three of a kind and (a/two) pair
        elif self_rank == 3 or self_rank == 1 or self_rank == 2:
            self_sorted = self_faces # we already got the index
            other_sorted = other_faces # we already got the index
        else:
            self_sorted = sorted([self.FACES_A.index(face) for face in self_faces], reverse=True)
            other_sorted = sorted([self.FACES_A.index(face) for face in other_faces], reverse=True)

        return self_sorted < other_sorted

    def __repr__(self):
        """Return a string representation for repr()."""
        return f"Hand({self.cards}"

    def __str__(self):
        """Return a string representation for str()."""
        return ', '.join(str(card.__str__()) for card in self.cards) + f'\t\t({self.evaluate()})'