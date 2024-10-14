import unittest
import main


class TestMain(unittest.TestCase):
    def test_input(self):
        test_guess = 2
        test_answer = 2
        result = main.check_guess(test_guess, test_answer)
        self.assertTrue(result)

    def test_input_guess_none(self):
        test_guess = None
        test_answer = 2
        result = main.check_guess(test_guess, test_answer)
        # self.assertEqual(test_answer, test_guess)


if __name__ == '__main__':
    unittest.main()
