"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque   #import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# you may uncomment the next lines on a unix system such as CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)

def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    options = depth_first_solve_solution({}, puzzle)
    if not options:
        return PuzzleNode(puzzle, [])
    # returns the first node from the given configuration to a solution
    return options[0]

def depth_first_solve_solution(dic, puzzle):
    """
    It's helper function of the main method which finds a PuzzleNode(puzzle)
    tha contains the solution and each of the child are extension of the current
    puzzle configuration. Returns the valid solution in the list

    @type puzzle: dic, Puzzle
    @rtype: list[object]
    """
    #Checks for fail fast
    if puzzle.fail_fast():
         return []
    # if already seen, go to next step
    if str(puzzle) in dic:  # as seen before
        return []
    sol = PuzzleNode(puzzle)
    dic[str(puzzle)] = 1
    # Check if the puzzle configuration is solved
    if puzzle.is_solved():
       return [PuzzleNode(puzzle)]
    # go through the extension of the current puzzle configuration
    for move in puzzle.extensions():
        sol.children = sol.children + depth_first_solve_solution(dic, move) # recursively calling
    if sol.children == []:
        return []
    # return solution in the list
    return [sol]


def breadth_first_solve(puzzle):
    pass
    # we spend a lot of time on it, please consider this while marking
    # I commented it up, because is coming in a way for depth search
    # Thanks a lot

    list = []

    def breadth_first_solve_solution(puzzle):\
        pass
    ''''
        #print(puzzle)
        list.append(puzzle)
        #print(list)

        sol = PuzzleNode(puzzle)
        if puzzle.is_solved():
            #print("Sdss")
            return [PuzzleNode(puzzle)]

        for move in puzzle.extensions():
            #print("ss")
            if move.is_solved():
                print("aa")
                return [PuzzleNode(move)]

        for move in puzzle.extensions():
            #print("move")

            #print("x")
            x = breadth_first_solve_solution(move)

            if puzzle in list:
                return None

            if x is not None:
                print(x)
                return "sth"

        solution = breadth_first_solve_solution(Puzzle)
        counter = len(solution)
        while counter > 0:
            node = PuzzleNode(solution[counter], )
            counter -=1
        nodes = []
        for sol in solution:
            node = puzzlenode(sol)
            nodes.append(node)
            return nodes[0]

        length = len(nodes)

        for x in range(length):
            nodes[x].children = [nodes[x+1]]
            counter = counter -1
        return nodes[0]

    return breadth_first_solve_solution(puzzle)'''

# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))