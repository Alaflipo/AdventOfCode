
def get_grid():
    with open('2022/day8/input.txt') as file:
        lines = file.readlines()
        grid = []
        height_grid = len(lines)
        width_grid = len(lines[0].strip())
        for line in lines:
            for height in line.strip():
                grid.append(height)
        return grid, width_grid, height_grid


def is_visible(row, height):
    for tree in row:
        if tree >= height:
            return False
    return True


def part1(grid, size):
    visible_trees = 0
    for i, height in enumerate(grid):
        left = is_visible(grid[int(i/size) * size: i], height)
        right = is_visible(grid[i + 1: int(i/size + 1) * size], height)
        up = is_visible(grid[i % size: i: size], height)
        down = is_visible(grid[i + size: -1: size], height)
        visible_trees += (left or right or up or down)
    return visible_trees


def amount_trees_visible(row, height):
    trees_visible = 0
    for tree in row:
        trees_visible += 1
        if tree >= height:
            return trees_visible
    return trees_visible


def part2(grid, size):
    scores = []
    for i, height in enumerate(grid):
        left = amount_trees_visible(
            grid[i - 1: int(i/size) * size - 1: -1], height)
        right = amount_trees_visible(
            grid[i + 1: int(i/size + 1) * size], height)
        up = amount_trees_visible(grid[i - size: i % size - 1: -size], height)
        down = amount_trees_visible(grid[i + size: -1: size], height)
        score = left * right * up * down
        scores.append(score)
    return max(scores)


def main():
    grid, width, height = get_grid()
    visible_trees = part1(grid, width)
    print(visible_trees)
    max_scenic_score = part2(grid, width)
    print(max_scenic_score)


if __name__ == "__main__":
    main()
