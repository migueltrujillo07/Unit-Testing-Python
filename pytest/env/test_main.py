import pytest

class TestExample():

    def test_sum_two_numbers(self):
        assert 10 + 10 == 20, 'Sorry the sum is incorrect'


    def test_subs_two_numbers(self):
        assert 10 - 10 == 0, 'Sorry, the substraccion is incorrect'
