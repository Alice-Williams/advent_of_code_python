from __future__ import annotations
import pathlib


class PuzzleSolver:
    def __init__(self, filename):
        self._file_path = pathlib.Path(__file__).parent.joinpath(filename)
        self._puzzle_inputs = self._read_puzzle_input_file()

    def _read_puzzle_input_file(self):
        with open(self._file_path) as file:
            raw_inputs = file.readlines()
        inputs = []
        for line in raw_inputs:
            clean_line = line.strip('\n')
            values = clean_line.split(' ')
            min_val, max_val = values[0].split('-')
            target_char = values[1].strip(':')
            password = values[2]
            inputs.append([int(min_val), int(max_val), target_char, password])
        return inputs

    def get_part_one_solution(self):
        valid_count = 0
        for input in self._puzzle_inputs:
            if self._valid_old_password(input):
                valid_count += 1
        return valid_count

    def _valid_old_password(self, input_vals):
        min_val, max_val, target_char, password = input_vals
        char_count = 0
        for char in password:
            if char == target_char:
                char_count += 1
        return min_val <= char_count <= max_val

    def get_part_two_solution(self):
        valid_count = 0
        for input in self._puzzle_inputs:
            if self._valid_new_password(input):
                valid_count += 1
        return valid_count

    def _valid_new_password(self, input_vals):
        first_idx, second_idx, target_char, password = input_vals
        if password[first_idx-1] == target_char:
            return password[second_idx-1] != target_char
        return password[second_idx-1] == target_char


def main():
    solver = PuzzleSolver('puzzle_input.txt')
    print(solver.get_part_two_solution())


if __name__ == '__main__':
    main()
