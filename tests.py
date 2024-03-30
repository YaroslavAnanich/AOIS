import unittest
from unittest.mock import patch
from io import StringIO
from main import generate_truth_table

class TestTruthTable(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_truth_table(self, mock_stdout):
        expression = 'a'
        variables = ['a']
        generate_truth_table(expression, variables)
        output = mock_stdout.getvalue()
        self.assertIn('a 0\n', output)

        expression = 'a & b'
        variables = ['a', 'b']
        generate_truth_table(expression, variables)
        output = mock_stdout.getvalue()
        self.assertIn('a b 0\n', output)

        expression = 'a | b & c'
        variables = ['a', 'b', 'c']
        generate_truth_table(expression, variables)
        output = mock_stdout.getvalue()
        self.assertIn('a b c 0\n', output)

        expression = 'a & b | c & d'
        variables = ['a', 'b', 'c', 'd']
        generate_truth_table(expression, variables)
        output = mock_stdout.getvalue()
        self.assertIn('a b c d 0\n', output)