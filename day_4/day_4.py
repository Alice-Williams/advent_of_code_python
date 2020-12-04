from __future__ import annotations
import pathlib
from typing import List, Dict


class PuzzleSolver:
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, filename: str):
        self._file_path = pathlib.Path(__file__).parent.joinpath(filename)
        self._puzzle_inputs = self._read_puzzle_input_file()

    def get_part_one_solution(self) -> int:
        count = 0
        for passport in self._puzzle_inputs:
            if self._has_required_fields(passport):
                count += 1
        return count

    def get_part_two_solution(self) -> int:
        count = 0
        for passport in self._puzzle_inputs:
            if self._has_required_fields(passport) and self._has_valid_fields(passport):
                count += 1
        return count

    def _read_puzzle_input_file(self) -> List[Dict[str, str]]:
        with open(self._file_path) as file:
            raw_inputs = file.read().splitlines()
        passports = []
        current_passport = dict()
        for line in raw_inputs:
            if not line:
                passports.append(current_passport)
                current_passport = dict()
            else:
                for info in line.split(' '):
                    field, value = info.split(':')
                    current_passport[field] = value
        passports.append(current_passport)
        return passports

    def _has_required_fields(self, passport: Dict[str, str]) -> bool:
        passport_keys = set(passport.keys())
        return all(field in passport_keys for field in self.REQUIRED_FIELDS)

    def _has_valid_fields(self, passport: Dict[str, str]) -> bool:
        return (
            self._is_valid_birth_year(passport['byr'])
            and self._is_valid_issue_year(passport['iyr'])
            and self._is_valid_expiration_year(passport['eyr'])
            and self._is_valid_height(passport['hgt'])
            and self._is_valid_hair_colour(passport['hcl'])
            and self._is_valid_eye_colour(passport['ecl'])
            and self._is_valid_passport_id(passport['pid'])
        )

    def _is_valid_birth_year(self, year_str: str) -> bool:
        min_year = 1920
        max_year = 2002
        return self._is_valid_year(year_str, min_year, max_year)

    def _is_valid_issue_year(self, year_str: str) -> bool:
        min_year = 2010
        max_year = 2020
        return self._is_valid_year(year_str, min_year, max_year)

    def _is_valid_expiration_year(self, year_str: str) -> bool:
        min_year = 2020
        max_year = 2030
        return self._is_valid_year(year_str, min_year, max_year)

    def _is_valid_year(self, year_str: str, min_year: int, max_year: int) -> bool:
        if not len(year_str) == 4:
            return False
        try:
            year_int = int(year_str)
        except TypeError:
            return False
        return min_year <= year_int <= max_year

    def _is_valid_height(self, height_str: str) -> bool:
        if height_str.endswith('in'):
            inches = int(height_str.strip('in'))
            return 59 <= inches <= 76
        if height_str.endswith('cm'):
            centimetres = int(height_str.strip('cm'))
            return 150 <= centimetres <= 193
        return False

    def _is_valid_hair_colour(self, hair_colour: str) -> bool:
        if len(hair_colour) != 7:
            return False
        if hair_colour[0] != '#':
            return False
        valid_hex_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
        return all(char in valid_hex_chars for char in hair_colour[1:])

    def _is_valid_eye_colour(self, eye_colour: str) -> bool:
        valid_eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        return eye_colour in valid_eye_colours

    def _is_valid_passport_id(self, passport_id: str) -> bool:
        if len(passport_id) != 9:
            return False
        try:
            int(passport_id)
        except TypeError:
            return False
        return True


def main():
    solver = PuzzleSolver('puzzle_input.txt')
    print(solver.get_part_two_solution())


if __name__ == '__main__':
    main()
