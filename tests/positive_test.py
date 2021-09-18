import pytest
from application.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_passed(self):
        assert self.calc.multiply(self, 2, 4) == 8

    def test_division_calc_passed(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_calc_passed(self):
        assert self.calc.subtraction(self, 4, 3) == 1

    def test_adding_calc_passed(self):
        assert self.calc.adding(self, 4, 2) == 6