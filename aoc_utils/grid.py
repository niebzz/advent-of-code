def display_grid(grid: list[list]):
    print("-----GRID-----")
    for row in grid:
        print(row)


def get_adjacent_coordinates(row: int, col: int, grid: list[list]) -> list(tuple):
    """Takes row, col integers as part of a grid (list of sublists 
    containing single-character elements) and returns the adjacent 
    rows, columns that are within the boundaries of the grid."""

    dr = set([max(0, row - 1), row, min(row + 1, len(grid) - 1)])
    dc = set([max(0, col - 1), col, min(col + 1, len(grid[row]) - 1)])

    return [x for x in [(r, c) for r in dr for c in dc] if x != (row, col)]
