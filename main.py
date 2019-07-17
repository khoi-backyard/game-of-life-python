import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GLIDER = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
SPACE_SHIP = np.array(
    [
        [0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0],
    ]
)


def randomGrid(N, alive_ratio=0.2):
    assert alive_ratio <= 1, "alive_ratio must be <= 1"
    return np.random.choice(
        [1, 0], N * N, p=[alive_ratio, 1 - alive_ratio]
    ).reshape(N, N)


def addPattern(i, j, pattern, grid):
    assert pattern.ndim == 2, "pattern dimension should be 2"
    grid[i : i + pattern.shape[0], j : j + pattern.shape[1]] = pattern


def main():
    grid = randomGrid(16, alive_ratio=0)
    addPattern(0, 0, SPACE_SHIP, grid)
    print(grid)
    pass


if __name__ == "__main__":
    main()
