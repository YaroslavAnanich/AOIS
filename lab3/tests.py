import RDNF as rd
import RKNF as rk
import RTDNF as rtd
import RTKNF as rtk
import TDNF as td
import TKNF as tk
import unittest


class RDTestLogicFunctions(unittest.TestCase):

    def rd_test_parse_infix(self):
        self.assertEqual(rd.parse_infix('a & b | c'), ['a', 'b', '&', 'c', '|'])

    def rd_test_evaluate_expression(self):
        self.assertTrue(rd.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': True, 'b': False, 'c': True}))
        self.assertFalse(rd.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': False, 'b': False, 'c': False}))
        self.assertTrue(rd.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': True, 'b': True, 'c': False}))
        self.assertTrue(rd.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': False, 'b': True, 'c': True}))
        self.assertFalse(rd.evaluate_expression(['a', 'b', '&', 'c', '|'], {'a': False, 'b': False, 'c': False}))

    def rd_test_create_truth_table(self):
        self.assertEqual(rd.create_truth_table(['a', 'b', '&', 'c', '|']), [
            [(False, False, False, False),
             (False, False, True, True),
             (False, True, False, False),
             (False, True, True, True),
             (True, False, False, False),
             (True, False, True, True),
             (True, True, False, True),
             (True, True, True, True)]

        ])

    def rd_test_sdnf_to_binary(self):
        self.assertEqual(rd.sdnf_to_binary('!a  b | !b  c'), ['(0,1)', '(0,1)'])

    def test_parse_infix(self):
        self.assertEqual(rk.parse_infix("a & b | c"), ['a', 'b', '&', 'c', '|'])

    def test_create_truth_table(self):
        self.assertEqual(rk.create_truth_table(['a', 'b', '|', 'c', '&']), [
            (False, False, False, False),
            (False, False, True, False),
            (False, True, False, False),
            (False, True, True, True),
            (True, False, False, False),
            (True, False, True, True),
            (True, True, False, False),
            (True, True, True, True)
        ])

    def test_sknf_to_binary(self):
        self.assertEqual(rk.sknf_to_binary("!a !b & c !d"), ['(1,1)', '(0,1)'])

    def test_group_by_units(self):
        self.assertEqual(rk.group_by_units(['(1,1)', '(0,1)']), {0: ['(1,1)'], 1: ['(0,1)']})

    def rtd_test_sdnf_to_binary(self):
        self.assertEqual(rtd.sdnf_to_binary('!a  b | !b  !c'), ['(0,1)', '(0,0)'])

    def rtk_test_sdnf_to_binary(self):
        self.assertEqual(tk.sknf_to_binary('!a  b | !b  c'), ['(0,1)', '(0,1)'])

    def rcd_test_sdnf_to_binary(self):
        self.assertEqual(rtd.sdnf_to_binary('!a  !b | !b  c'), ['(0,0)', '(0,1)'])

    def dtest_parse_infix(self):
        self.assertEqual(rk.parse_infix("a & b | c"), ['a', 'b', '&', 'c', '|'])


    def cctest_create_truth_table(self):
        self.assertEqual(rk.create_truth_table(['a', 'b', '|', 'c', '&']), [
            (False, False, False, False),
            (False, False, True, False),
            (False, True, False, False),
            (False, True, True, True),
            (True, False, False, False),
            (True, False, True, True),
            (True, True, False, False),
            (True, True, True, True)
        ])

    def atest_sknf_to_binary(self):
        self.assertEqual(rk.sknf_to_binary("!a !b & c !d"), ['(1,1)', '(0,1)'])

    def btest_group_by_units(self):
        self.assertEqual(rk.group_by_units(['(1,1)', '(0,1)']), {0: ['(1,1)'], 1: ['(0,1)']})

class RKTestLogicFunctions(unittest.TestCase):

    def test_parse_infix(self):
        self.assertEqual(rk.parse_infix("a & b | c"), ['a', 'b', '&', 'c', '|'])


    def test_create_truth_table(self):
        self.assertEqual(rk.create_truth_table(['a', 'b', '|', 'c', '&']), [
            (False, False, False, False),
            (False, False, True, False),
            (False, True, False, False),
            (False, True, True, True),
            (True, False, False, False),
            (True, False, True, True),
            (True, True, False, False),
            (True, True, True, True)
        ])

    def test_sknf_to_binary(self):
        self.assertEqual(rk.sknf_to_binary("!a !b & c !d"), ['(1,1)', '(0,1)'])

    def test_group_by_units(self):
        self.assertEqual(rk.group_by_units(['(1,1)', '(0,1)']), {0: ['(1,1)'], 1: ['(0,1)']})


class RTDTestLogicFunctions(unittest.TestCase):
    def rtd_test_sdnf_to_binary(self):
        self.assertEqual(rtd.sdnf_to_binary('!a  b | !b  c'), ['(0,1)', '(0,1)'])


class RTKTestLogicFunctions(unittest.TestCase):
    def rtk_test_sdnf_to_binary(self):
        self.assertEqual(rtk.sknf_to_binary('!a  b | !b  c'), ['(0,1)', '(0,1)'])


class TDTestLogicFunctions(unittest.TestCase):
    def rtk_test_sdnf_to_binary(self):
        self.assertEqual(td.sdnf_to_binary('!a  b | !b  c'), ['(0,1)', '(0,1)'])


class TKTestLogicFunctions(unittest.TestCase):
    def rtk_test_sdnf_to_binary(self):
        self.assertEqual(tk.sknf_to_binary('!a  b | !b  c'), ['(0,1)', '(0,1)'])

    def rtk_test_sdn2f_to_binary(self):
        self.assertEqual(td.sdnf_to_binary('!a  b | !b  c'), ['(1,0)', '(1,0)'])

class TTestLogicFunctions(unittest.TestCase):
    def rtk_test_ssdnf_to_binary(self):
        self.assertEqual(tk.generate_truth_table("((a | b) -> (a & c))", 3), 'a !b c & a !b !c & !a b c & !a !b c')
