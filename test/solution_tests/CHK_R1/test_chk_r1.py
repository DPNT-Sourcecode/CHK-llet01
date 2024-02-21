from lib.solutions.CHK import checkout_solution

class TestCHK_R1():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_multiple(selfs):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_offer(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("AAAAAA") == 260

    def test_checkout_offer_and_individual(self):
        assert checkout_solution.checkout("AAAAAAAA") == 360
        assert checkout_solution.checkout("AAAAABBB") == 305
