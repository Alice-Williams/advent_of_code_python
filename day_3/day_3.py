from __future__ import annotations
import pathlib
from typing import List

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)


class PuzzleSolver:
    TREE_CHAR = '#'

    def __init__(self, filename):
        self._file_path = pathlib.Path(__file__).parent.joinpath(filename)
        self._puzzle_inputs = self._read_puzzle_input_file()

    def _read_puzzle_input_file(self) -> List[str]:
        with open(self._file_path) as file:
            inputs = [line.strip('\n') for line in file.readlines()]
        return inputs

    def get_part_one_solution(self) -> int:
        slope = Coordinates(3, 1)
        return self._get_collision_count_for_slope(slope)

    def get_part_two_solution(self) -> int:
        slopes = [Coordinates(1, 1), Coordinates(3, 1), Coordinates(5, 1), Coordinates(7, 1), Coordinates(1, 2)]
        collisions_counts = [self._get_collision_count_for_slope(slope) for slope in slopes]
        return self._get_product(collisions_counts)

    def _get_product(self, values: List[int]) -> int:
        total_product = 1
        for value in values:
            total_product *= value
        return total_product

    def _get_collision_count_for_slope(self, slope: Coordinates) -> int:
        position_coords = self._calculate_positions(slope)
        collision_count = self._get_tree_collision_count(position_coords)
        return collision_count

    def _get_tree_collision_count(self, position_coords: List[Coordinates]) -> int:
        collision_count = 0
        row_length = len(self._puzzle_inputs[0])
        for position in position_coords:
            position_char = self._puzzle_inputs[position.y][position.x % row_length]
            if position_char == self.TREE_CHAR:
                collision_count += 1
        return collision_count

    def _calculate_positions(self, movement: Coordinates) -> List[Coordinates]:
        start = Coordinates(0, 0)
        row_count = len(self._puzzle_inputs)
        current_coord = start
        positions = []
        for _ in range(row_count // movement.y):
            positions.append(current_coord)
            current_coord += movement
        return positions


def main():
    solver = PuzzleSolver('puzzle_input.txt')
    print(solver.get_part_two_solution())


if __name__ == '__main__':
    main()
