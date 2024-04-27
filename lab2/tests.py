import unittest
import main

class TestLogicFunctions(unittest.TestCase):

    def test_parse_infix(self):
        self.assertEqual(main.parse_infix('(a & b) | c'), ['a', 'b', '&', 'c', '|'])
        self.assertEqual(main.parse_infix('(a | b) & !c'), ['a', 'b', '|', 'c', '!', '&'])
        self.assertEqual(main.parse_infix('(a | b) - d'), ['a', 'b', '|', 'd', '-'])
        self.assertEqual(main.parse_infix('(a | b) ~ d'), ['a', 'b', '|', 'd', '~'])

    def test_evaluate_expression(self):
        self.assertTrue(main.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': True, 'b': False, 'c': True}))
        self.assertFalse(main.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': False, 'b': False, 'c': False}))
        self.assertTrue(main.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': True, 'b': True, 'c': False}))
        self.assertFalse(main.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': False, 'b': True, 'c': False}))

    def test_create_truth_table(self):
        truth_table, variables, int_result = main.create_truth_table(['a', 'b', '&', 'c', '|'])
        self.assertEqual(variables, ['a', 'b', 'c'])
        self.assertEqual(len(truth_table), 8)
        self.assertEqual(int_result, '01010111')

    def test_generate_sdnf(self):
        truth_table, variables, _ = main.create_truth_table(['a', 'b', '&', 'c', '|'])
        sdnf, sdnf_numeric_form = main.generate_sdnf(truth_table, variables)
        self.assertEqual(sdnf, '(!a & !b & c) | (!a & b & c) | (a & !b & c) | (a & b & !c) | (a & b & c)')
        self.assertEqual(sdnf_numeric_form, [1, 3, 5, 6, 7])

    def test_generate_sknf(self):
        truth_table, variables, _ = main.create_truth_table(['a', 'b', '&', 'c', '|'])
        sknf, sknf_numeric_form = main.generate_sknf(truth_table, variables)
        self.assertEqual(sknf, '(a | b | c) & (a | !b | c) & (!a | b | c)')
        self.assertEqual(sknf_numeric_form, [0, 2, 4])

if __name__ == '__main__':
    unittest.main()