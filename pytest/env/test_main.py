import pytest

class TestExample():

    def setup_method(self):
        pass

    def teardown_method(self):
        pass


    def test_sum_two_numbers(self):
        assert 10 + 10 == 20, 'Sorry the sum is incorrect'


    def test_subs_two_numbers(self):
        assert 10 - 10 == 0, 'Sorry, the substraccion is incorrect'

class TestExample2():

    def test_mul_two_numberss(self):
        assert 2 * 10 == 20, 'Sorry but the multiplication is incorrect'

