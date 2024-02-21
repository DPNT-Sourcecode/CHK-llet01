from lib.solutions.CHK import checkout_solution


class TestCHK_R1():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_multiple(selfs):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_offer(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout_offer_and_individual(self):
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAABBB") == 255

    def test_checkout_BOGOF_rule(self):
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEB") == 120
        assert checkout_solution.checkout("EEEBB") == 150
        assert checkout_solution.checkout("BBEEE") == 150
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("BEBEEE") == 160

    def test_checkout_BOGOF_f_rule(self):
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("FFBEBEEEFFFF") == 200

    def test_checkout_items_in_set_offer(self):
        assert checkout_solution.checkout("XTS") == 45
        assert checkout_solution.checkout("XTST") == 65
        assert checkout_solution.checkout("XTSTXS") == 90
        assert checkout_solution.checkout("XTSTXSSS") == 130
        assert checkout_solution.checkout("XTFFSTXS") == 110




