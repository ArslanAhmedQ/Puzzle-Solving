# PuzzleSolving
Solving different types of puzzle including Soduku, Peg Solitaire, Word ladder, and MN puzzle. 
We will investigates a class of puzzles that have the following features in common:
Full information: all information about the puzzle configuration at any given point is visible to the solver;
there are no hidden or random aspects
Well-defined extensions: The legal extensions from a given puzzle configuration to new configurations
is given
Well-defined solution: It means for the puzzled to be in a solved state.

Abstract Puzzle class has methods:
is_solved: it returns True or False, depending on whether the puzzle is in a solved configuration or not.
extensions: it returns a list of extensions from the current to the new puzzle configurations that are
a always single step away.
fail_fast: it returns True if it is clear that the current puzzle configuration can never be completed, via the sequence of extensions to a complete solved state
