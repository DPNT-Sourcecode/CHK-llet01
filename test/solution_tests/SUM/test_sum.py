from lib.solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_out_of_range(self):
        try:
            sum_solution.compute(101, 2)
        except Exception as e:
            assert e.__class__.__name__ == "ValueError"
            assert str(e) == "x should be between 0 and 100"

    def test_sum_not_int(self):
        try:
            sum_solution.compute("a", 2)
        except Exception as e:
            assert e.__class__.__name__ == "ValueError"
            assert str(e) == "x and y should be integers"