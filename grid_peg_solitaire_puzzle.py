from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self, other):
        """
        Return that
        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool
        """
        return self._marker == other._marker and self._marker_set == other. _marker_set

    def __str__(self):
        """
        Return a human-readable string representation of GridPegSolitairePuzzle self.
        @type self: GridPegSolitairePuzzle
        @rtype: String

        # >>> grid1 = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"],["*", "*", "*", "*", "*"]]
        # >>> puzzle = GridPegSolitairePuzzle(grid1, {"*", ".", "#"})
        # >>> print(puzzle)
        # * * * * *
        # * * * * *
        # * * * * *
        # * * . * *
        # * * * * *
        """

        grid =''
        for lists in self._marker:
            result = ''
            for column in lists:
                result += (column) + " "
            grid += result
            grid += "\n"


        return_grid = "".join(grid)
        string_list = return_grid.strip()

        return string_list

    def extensions(self):
        """
        Retur a list of extensions of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]

        >>> grid = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"],["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> L1 = list(gpsp.extensions())
        >>> grid[-1] = ["*", "*", "*", "*", "*"]
        >>> L2 = [GridPegSolitairePuzzle(grid, {"*", ".", "#"})]
        >>> len(L1) == len(L2)
        False
        """
        marker, marker_set = self._marker, self._marker_set
        if self.is_solved():
            return []

        extensions_list = []
        for row in range(len(marker) - 1):
            for column in range(len(marker) - 1):

                if column < len(marker) - 2 and marker[row][column] == "." and marker[row][column + 1] == "*" and marker[row][column + 2] == "*":
                    new = marker
                    new[row][column] = "*"
                    new[row][column + 1] = "."
                    new[row][column + 2] = "."
                    z = GridPegSolitairePuzzle(new, marker_set)
                    extensions_list.append(z)

                if row < len(marker) - 2 and marker[row][column] == "*" and marker[row + 1][column] == "*" and marker[row + 2][column] == ".":
                    new = marker
                    new[row][column] = "."
                    new[row + 1][column] = "."
                    new[row + 2][column] = "*"
                    z = GridPegSolitairePuzzle(new, marker_set)
                    extensions_list.append(z)

                if column < len(marker) - 2 and marker[row][column] == "*" and marker[row][column + 1] == "*" and marker[row][column + 2] == ".":
                    new = marker
                    new[row][column] = "."
                    new[row][column + 1] = "."
                    new[row][column + 2] = "*"
                    z = GridPegSolitairePuzzle(new, marker_set)
                    extensions_list.append(z)

                if row < len(marker) - 2 and marker[row][column] == "." and marker[row + 1][column] == "*" and marker[row + 2][column] == "*":
                    new = marker
                    new[row][column] = "*"
                    new[row + 1][column] = "."
                    new[row + 2][column] = "."
                    z = GridPegSolitairePuzzle(new, marker_set)
                    extensions_list.append(z)

        return extensions_list

    def is_solved(self):
        """
        Return whether GridPegSolitairePuzzle self is solved.

        @type self: GridPegSolitairePuzzle
        @rtype: bool

        >>> grid1 = [[".", ".", ".", ".", "."],["*", ".", ".", ".", "."],[".", ".", ".", ".", "."], [".", ".", ".", ".", "."],[".", ".", ".", ".", "."]]
        >>> gridPuzzle = GridPegSolitairePuzzle(grid1,{"*",".","#"})
        >>> gridPuzzle.is_solved()
        True
        >>> grid2 = [["*", ".", ".", ".", "."],["*", "*", ".", ".", "."],[".", ".", ".", ".", "."], [".", ".", ".", ".", "."],[".", ".", ".", ".", "."]]
        >>> gridPuzzle = GridPegSolitairePuzzle(grid2,{"*",".","#"})
        >>> gridPuzzle.is_solved()
        False
        """
        marker = self._marker
        counter = 0
        for row in marker:
            for column in row:
                if column == "*":
                    counter += 1
                elif counter >= 2:
                    return False
        if counter == 1:
            return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))