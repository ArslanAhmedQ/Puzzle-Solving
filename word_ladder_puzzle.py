from puzzle import Puzzle

class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle | Any
        @rtype: bool

        >>> initial = (WordLadderPuzzle("came", "same", {"came", "same", "lame"}))
        >>> other1 = (WordLadderPuzzle("came", "same", {"came", "same", "lame"}))
        >>> other2 = (WordLadderPuzzle("came", "lame", {"came", "same", "lame"}))
        >>> initial.__eq__(other1)
        True
        >>> initial.__eq__(other2)
        False
        """

        return (type(self) == type(other) and
                self._from_word == other._from_word and
                self._to_word == other._to_word and
                self._word_set == other._word_set)

    def __str__(self):
        """
        Return a  string representation of WordLadderPuzzle self.

        >>> string = WordLadderPuzzle("on", "no", {"on", "no"})
        >>> print(string)
        From on To no
        """
        return ("From {} To {}".format(self._from_word, self._to_word))

    def extensions(self):
        """
        Return list of extensions of WordLadderPuzzle self.
        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> W = WordLadderPuzzle("came", "same", {"came", "same", "lame"})
        >>> W1 = list(W.extensions())
        >>> W2 = list(W.extensions())
        >>> W1 == W2
        True
        >>> all([W in W2 for W in W1])
        True
        >>> all([W in W1 for W in W2])
        True
        """

        # convenient names
        from_word, to_word, word_set = self._from_word, self._to_word, self._word_set
        return_list = []
        temp_word = self._from_word
        chars = self._chars

        words_list = []
        if not from_word == to_word:    # given word is not equals to word,
            for y in range (len(temp_word)): # alphabet in temporary word
                for x in range(len(chars)):     # alphabet in chars

                    temp_word = temp_word[:y] + chars[x] + temp_word[y+1:]
                    # if words is in words.txt file, add the word, otherwise not
                    if temp_word in word_set:
                        words_list.append(temp_word)
                temp_word = from_word

        for words in words_list:
            return_list.append(WordLadderPuzzle(words, to_word, word_set))
        return return_list

    def is_solved(self):
        """
        Return whether WordLadderPuzzle self is solved.

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> x = (WordLadderPuzzle("to", "too", {"to", "too"}))
        >>> x.is_solved()
        False
        >>> y = (WordLadderPuzzle("to", "to", {"to", "too"}))
        >>> y.is_solved()
        True
        """
        # solved when the from_word is same as to_word
        return self._from_word == self._to_word

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
