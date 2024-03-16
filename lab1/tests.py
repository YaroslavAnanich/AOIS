import unittest
import numpy as np
import binary_operations as bin


class TestDirectInverseAdditionalCode(unittest.TestCase):

    def test_direct_code_positive_number(self):
        number = 50
        expected_output = np.array([0, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.direct_code(number).tolist(), expected_output.tolist())

    def test_direct_code_negative_number(self):
        number = -50
        expected_output = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        self.assertEqual(bin.direct_code(number).tolist(), expected_output.tolist())

    def test_inverse_code_positive_number(self):
        direct_input = np.array([0, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        expected_output = np.array([0, 0, 1, 0, 1, 1, 0, 1], dtype=object)
        self.assertEqual(bin.inverse_code(direct_input).tolist(), expected_output.tolist())

    def test_inverse_code_negative_number(self):
        direct_input = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        expected_output = np.array([1, 0, 0, 1, 0, 1, 1, 0], dtype=object)
        self.assertEqual(bin.inverse_code(direct_input).tolist(), expected_output.tolist())

    def test_additional_code_positive_number(self):
        inverse_input = np.array([0, 0, 1, 0, 1, 1, 0, 1], dtype=object)
        expected_output = np.array([0, 0, 1, 0, 1, 1, 0, 1], dtype=object)
        self.assertEqual(bin.additional_code(inverse_input).tolist(), expected_output.tolist())

    def test_additional_code_negative_number(self):
        inverse_input = np.array([1, 0, 0, 1, 0, 1, 1, 0], dtype=object)
        expected_output = np.array([1, 0, 0, 1, 0, 1, 1, 0], dtype=object)
        self.assertEqual(bin.additional_code(inverse_input).tolist(), expected_output.tolist())

    def test_direct_sum(self):
        direct1 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        direct2 = np.array([1, 0, 0, 0, 0, 0, 0, 1], dtype=object)
        expected_output = np.zeros(8, dtype=object)
        self.assertEqual(bin.direct_sum(direct1, direct2).tolist(), expected_output.tolist())

    def test_additional_sum(self):
        additional1 = np.array([0, 0, 0, 0, 1, 0, 0, 1], dtype=object)
        additional2 = np.array([1, 0, 0, 0, 1, 0, 0, 1], dtype=object)
        expected_output = np.zeros(8, dtype=object)
        self.assertEqual(bin.additional_sum(additional1, additional2).tolist(), expected_output.tolist())

    def test_additional_subtraction(self):
        additional1 = np.array([0, 1, 0, 1, 1, 0, 0, 1], dtype=object)
        additional2 = np.array([0, 1, 0, 1, 1, 0, 0, 1], dtype=object)
        expected_output = np.zeros(8, dtype=object)
        self.assertEqual(bin.additional_subtraction(additional1, additional2).tolist(), expected_output.tolist())

    def test_moving(self):
        direct_input = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        index = 2
        expected_output = np.array([1, 0, 0, 1, 1, 0, 0, 1], dtype=object)
        self.assertEqual(bin.moving(index, direct_input).tolist(), expected_output.tolist())

    def test_direct_multiplication(self):
        direct1 = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=object)
        direct2 = np.array([0, 1, 0, 1, 1, 0, 0, 1], dtype=object)
        expected_output = np.array([0, 1, 0, 0, 0, 1, 0, 1], dtype=object)
        self.assertEqual(bin.direct_multiplication(direct1, direct2).tolist(), expected_output.tolist())
