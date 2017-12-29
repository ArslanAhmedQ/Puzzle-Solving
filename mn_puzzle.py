from puzzle import Puzzle

class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    def __eq__(self, other):
        """
        Return whether MNPuzzle self is equivalent to other.

        @type self: MNPuzzlePuzzle
        @type other: MNPuzzlePuzzle | Any
        @rtype: bool

        >>> played_grid  = (("*", "2", "3"), ("1", "4", "5"), ("7", "6", "8"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"), ("6", "7", "8"))
        >>> m1 = MNPuzzle(played_grid, target_grid)
        >>> m2 = MNPuzzle(played_grid, target_grid)
        >>> m1.__eq__(m2)
        True
        >>> played_grid1  = (("*", "2", "3"), ("1", "4", "5"), ("6", "8", "7")) # m3 is using this set of grid
        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"), ("6", "7", "8"))
        >>> m3 = MNPuzzle(played_grid1, target_grid1)
        >>> m1.__eq__(m3)
        False
        """

        return (type(self) == type(other) and
                self.from_grid == other.from_grid and
                self.to_grid == other.to_grid)

    def __str__(self):
        """
        Return a string representation of MNPuzzle self

        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> m1 = MNPuzzle(start_grid, target_grid)
        >>> print(m1)
        * |2 |3 |
        1 |4 |5 |
        """

        # convenient names
        n, m, from_grid, to_grid = self.n, self.m, self.from_grid, self.to_grid
        working_list = []
        for row in range(n):
            for column in range(m):
                # add just divider if number more than 10
                if not from_grid[row][column] == "*" and int(from_grid[row][column]) > 9:
                    working_list.append(from_grid[row][column] + "|")
                # add space and divider for "*" and number less than 10
                else:
                    working_list.append(from_grid[row][column] + " |")
            working_list.append("\n")
        # removes the unwanted spaces
        string_list = "".join(working_list)
        string_list = string_list.strip()
        return string_list

    def extensions(self):
        """
        Return list of extensions of MNPuzzle self.

        @type self: MNPuzzlePuzzle
        @rtype: list[MNPuzzlePuzzle]

        >>> grid1 = (("2", "1", "3"), ("4", "5", "*"))        # start grid
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> s = MNPuzzle(grid1, target_grid)
        >>> grid3  =  (("2", "1", "3"), ("4", "*", "5"))       # extension of grid 1
        >>> MN1 = list(s.extensions())
        >>> MN2 = MNPuzzle(grid3, target_grid)
        >>> MN2 in MN1
        True
        """
        # convenient names
        from_grid, to_grid = self.from_grid, self.to_grid
        #find the "*" coordinate from the from_grid
        count_row = 0
        for row in from_grid:
            count_column = 0
            for column in row:
                if column == "*":
                    r = count_row
                    c = count_column    # empty space in (x, y)
                count_column += 1
            count_row += 1

        # helper functions
        def swap_up(self):
            """
            Return object of up movement extension of MNPuzzle self.

            @type self: MNPuzzle
            @rtype: MNPuzzle

            """
            temp_cell = from_grid[r-1][c]  # Assigning the temporary cel
            working_grid = []
            for elements in from_grid:
                working_grid.append(list(elements)) # change it to list format
            if r == 0:    # row is 0, can't move up
                return None
            else:
                working_grid[r][c] = temp_cell
                working_grid[r-1][c] = "*"  # place the "*" towards up

            new_grid = []
            for elements in working_grid:
                new_grid.append(tuple(elements))
            new_grid = tuple(new_grid)  # return in tuple format

            return MNPuzzle(new_grid, to_grid)

        def swap_down(self):
            """
            Return object of down movement extension of MNPuzzle self.

            @type self: MNPuzzle
            @rtype: MNPuzzle

            """

            # can't move down if it is all thw way down
            if r == len(from_grid)-1:
                return None
            temp_cell = from_grid[r+1][c] # Assigning the temporary cell
            working_grid=[]
            for elements in from_grid:
                working_grid.append(list(elements))
            else:
                working_grid[r][c] = temp_cell
                working_grid[r+1][c] = "*"  # place the "*" towards down

            new_grid = []
            for elements in working_grid:
                new_grid.append(tuple(elements))
            new_grid = tuple(new_grid)

            return MNPuzzle(new_grid, to_grid)

        def swap_left(self):
            """
            Return object of left movement extension of MNPuzzle self.

            @type self: MNPuzzle
            @rtype: object

            """

            temp_cell = from_grid[r][c-1] # Assigning the temporary cell
            working_grid=[]
            for elements in from_grid:
                working_grid.append(list(elements))
            if c == 0: # cant move left, if column is  0
                return None
            else:
                working_grid[r][c] = temp_cell
                working_grid[r][c-1] = "*"  # place the "*" towards left

            new_grid = []
            for elements in working_grid:
                new_grid.append(tuple(elements))
            new_grid = tuple(new_grid)

            return MNPuzzle(new_grid, to_grid)

        def swap_right(self):
            """
            Return object of right movement extension of MNPuzzle self.

            @type self: MNPuzzle
            @rtype: object

            """

            if c == len(from_grid[0])-1:  # can't move right, if is all thw way right
                return None
            temp_cell = from_grid[r][c+1]  # Assigning the temporary cell
            working_grid=[]
            for elements in from_grid:
                working_grid.append(list(elements))
            else:
                working_grid[r][c] = temp_cell
                working_grid[r][c+1] = "*"  # place the "*" towards right

            new_grid = []
            for elements in working_grid:
                new_grid.append(tuple(elements))
            new_grid = tuple(new_grid)

            return MNPuzzle(new_grid, to_grid)

        # appends all the moves in final list
        final_list = []
        final_list.append(swap_up(self))
        final_list.append(swap_down(self))
        final_list.append(swap_left(self))
        final_list.append(swap_right(self))
        # If any extension is None, it removes it and return the possible one in the final list
        while True:
            if None in final_list:
                final_list.remove(None)
            else:
                break
        return final_list

    def is_solved(self):
        """
        Return whether MNPuzzle self is solved.

        @type self: MNPuzzle
        @rtype: bool

        >>> start_grid  =  (("1", "2", "3"), ("4", "5", "*"), ("6", "7", "8"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"), ("6", "7", "8"))
        >>> m1 = MNPuzzle(start_grid, target_grid)
        >>> m1.is_solved()
        True
        >>> start_grid1  = (("*", "2", "3"), ("1", "4", "5"), ("6", "8", "7")) # m2 is using this set of grid
        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"), ("6", "7", "8"))
        >>> m2 = MNPuzzle(start_grid1, target_grid1)
        >>> m2.is_solved()
        False
        """
        # convenient names
        from_grid, to_grid = self.from_grid, self.to_grid
        return from_grid == to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))

    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))

