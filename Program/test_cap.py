import unittest
import Demo


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = Demo.text_cap(text)
        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = Demo.text_cap(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
