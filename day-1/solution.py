import math


def solve_part1(lines):
    """Count times dial ENDS on 0 after a rotation."""
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def solve_part2(lines):
    """Count times dial PASSES THROUGH 0 during any rotation."""
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == 'R':
            # Moving right (toward higher numbers)
            # We cross 0 each time we wrap from 99 -> 0
            zeros_crossed = (position + distance) // 100
        else:
            # Moving left (toward lower numbers)
            # We cross 0 each time we wrap from 0 -> 99
            zeros_crossed = math.ceil(position / 100) - math.ceil((position - distance) / 100)

        zero_count += zeros_crossed

        # Update position for next iteration
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

    return zero_count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    print(f"Part 1: {solve_part1(lines)}")
    print(f"Part 2: {solve_part2(lines)}")
