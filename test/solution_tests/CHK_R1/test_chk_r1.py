from lib.solutions.CHK import checkout_solution

class TestCHK_R1():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_multiple(selfs):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_offer(self):
        assert checkout_solution.checkout("AAA") == 130
    