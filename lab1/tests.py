import unittest
import numpy as np
import binary_operations as bin
import ieee754


class TestDirectInverseAdditionalCode(unittest.TestCase):

    def test_direct_code_positive_number(self):
        number = 50
        expected_output = np.array([0, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.direct_code(number).tolist(), expected_output.tolist())

    def test_direct_code_negative_number(self):
        number = -50
        expected_output = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.direct_code(number).tolist(), expected_output.tolist())

    def test_inverse_code_negative_number(self):
        direct_input = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        expected_output = np.array([1, 1, 0, 0, 1, 1, 0, 1], dtype=object)
        self.assertEqual(bin.inverse_code(direct_input).tolist(), expected_output.tolist())

    def test_additional_code_positive_number(self):
        inverse_input = np.array([0, 0, 1, 0, 1, 1, 0, 1], dtype=object)
        expected_output = np.array([0, 0, 1, 0, 1, 1, 0, 1], dtype=object)
        self.assertEqual(bin.additional_code(inverse_input).tolist(), expected_output.tolist())

    def test_additional_code_negative_number(self):
        inverse_input = np.array([0, 0, 0, 1, 0, 1, 1, 0], dtype=object)
        expected_output = np.array([0, 0, 0, 1, 0, 1, 1, 0], dtype=object)
        self.assertEqual(bin.additional_code(inverse_input).tolist(), expected_output.tolist())

    def test_direct_sum(self):
        direct1 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        direct2 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        expected_output = np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.direct_sum(direct1, direct2).tolist(), expected_output.tolist())

    def test_additional_sum(self):
        additional1 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        additional2 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        expected_output = np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.additional_sum(additional1, additional2).tolist(), expected_output.tolist())

    def test_additional_subtraction(self):
        additional1 = np.array([0, 1, 0, 1, 1, 0, 0, 1], dtype=object)
        additional2 = np.array([0, 1, 0, 1, 1, 0, 0, 1], dtype=object)
        expected_output = np.zeros(8, dtype=object)
        self.assertEqual(bin.additional_subtraction(additional1, additional2).tolist(), expected_output.tolist())

    def test_moving(self):
        direct_input = np.array([0, 0, 0, 1, 0, 0, 1, 0], dtype=object)
        index = 1
        expected_output = np.array([0, 0, 1, 0, 0, 1, 0, 0], dtype=object)
        self.assertEqual(bin.moving(index, direct_input).tolist(), expected_output.tolist())

    def test_direct_multiplication(self):
        direct1 = np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=object)
        direct2 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        expected_output = np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.direct_multiplication(direct1, direct2).tolist(), expected_output.tolist())

    def test_comparison_less(self):
        self.assertTrue(bin.comparison_less([1, 2, 3], [1, 2, 4]))
        self.assertFalse(bin.comparison_less([1, 2, 3], [1, 2, 3]))

    def test_decimal_to_binary(self):
        self.assertEqual(bin.decimal_to_binary(5), '00101')
        self.assertEqual(bin.decimal_to_binary(10, 8), '00001010')

    def test_float_to_binary(self):
        self.assertEqual(bin.float_to_binary(5.25), '101.01')
        self.assertEqual(bin.float_to_binary(0.5), '0.1')

    def test_normalize_binary(self):
        self.assertEqual(bin.normalize_binary('101.01'), ('1.0101', 2))

    def test_binary_to_ieee754(self):
        self.assertEqual(bin.binary_to_ieee754('1001.101'), ieee754.IEEE754Number)


    def test_normalize_ieee754_mantissa(self):
        self.assertEqual(bin.normalize_ieee754_mantissa('1.0101', 1), '0.10101')


    def test_string_to_numpy(self):
        self.assertNotEquals(bin.string_to_numpy('1'), np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object))

    def test_mantissa_sum(self):
        self.assertEqual(bin.mantissa_sum('1.01', '1.01'), '10.000010')

    # def test_ieee754_sum(self):
    #     self.assertEqual(bin.ieee754_sum(ieee_first, ieee_second), 'IEEE754Number object')
