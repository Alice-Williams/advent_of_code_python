from __future__ import annotations
from typing import List
import pathlib


class PuzzleSolver:
    TARGET_VALUE = 2020

    def __init__(self, filename):
        self._file_path = pathlib.Path(__file__).parent.joinpath(filename)
        self._puzzle_inputs = self._read_puzzle_input_file()

    def _read_puzzle_input_file(self):
        with open(self._file_path) as file:
            raw_inputs = file.readlines()
            inputs = [int(line.strip('\n')) for line in raw_inputs]
            return inputs

    def get_solution(self, values_count) -> [int, int]:
        """Tries to find a number of values in self._puzzle_inputs that sum to self.TARGET_VALUE"""
        sum_values = self._get_sum_values(values_count)
        product = self._multiply_values(sum_values)
        return sum_values, product

    def _multiply_values(self, values):
        product = 1
        for val in values:
            product *= val
        return product

    def _get_sum_values(self, values_count):
        totals = {i: {} for i in range(1, values_count)}
        for value in self._puzzle_inputs:
            pair_val = self.TARGET_VALUE - value
            if pair_val in totals[values_count-1]:
                other_elements = totals[values_count-1][pair_val]
                return [value, *other_elements]
            for count in reversed(range(1, values_count-1)):
                for sub_total, elements in totals[count].items():
                    new_sub_total = value + sub_total
                    if new_sub_total < self.TARGET_VALUE and new_sub_total not in totals[count+1]:
                        totals[count+1][new_sub_total] = [value, *elements]
            if value not in totals[1]:
                totals[1][value] = [value]


def main():
    solver = PuzzleSolver('puzzle_input.txt')
    print(solver.get_solution(3))


if __name__ == '__main__':
    main()
