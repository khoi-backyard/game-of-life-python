import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def randomGrid(N, alive_ratio=0.2):
    assert alive_ratio <= 1, "alive_ratio must be <= 1"
    return np.random.choice([1, 0], N * N, p=[alive_ratio, 1 - alive_ratio]).reshape(
        N, N
    )


def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            top_left = grid[(i - 1) % N, (j - 1) % N]
            top = grid[(i - 1) % N, j]
            top_right = grid[(i - 1) % N, (j + 1) % N]
            left = grid[i, (j - 1) % N]
            right = grid[i, (j + 1) % N]
            bottom_left = grid[(i + 1) % N, (j - 1) % N]
            bottom = grid[(i + 1) % N, j]
            bottom_right = grid[(i + 1) % N, (j + 1) % N]
            neighbors_count = (
                top_left
                + top
                + top_right
                + left
                + right
                + bottom_left
                + bottom
                + bottom_right
            )

            if grid[i, j] == 1 and (neighbors_count < 2 or neighbors_count > 3):
                newGrid[i, j] = 0
            elif neighbors_count == 3:
                newGrid[i, j] = 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return (img,)


def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument(
        "--size", dest="grid_size", type=int, default=16, help="the grid size"
    )
    parser.add_argument(
        "--interval", dest="interval", type=int, default=20, help="the update interval"
    )
    args = parser.parse_args()

    GRID_SIZE = args.grid_size
    interval = args.interval

    grid = randomGrid(GRID_SIZE)

    fig, ax = plt.subplots()
    plt.axis("off")
    img = ax.imshow(grid, interpolation="nearest")
    ani = animation.FuncAnimation(
        fig,
        update,
        fargs=(img, grid, GRID_SIZE),
        frames=10,
        interval=interval,
    )
    plt.show()


if __name__ == "__main__":
    main()
