import unittest, cmath
from math import isclose
"""
This class is a test class used to test the divComplex fuction.

Example:

num1 = 10 + 12j
num2 = 5 + 2j
print(divComplex(num1,num2))

Output
----------------------
(2.5517+1.3793j)

"""
class divComplexTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_positive_all(self):
        self.assertEqual(divComplex(1 + 2j, 3 + 4j), (0.44+0.08j), "Test failed on all positive")
    #Test all negative.
    def test_negative_all(self):
        self.assertAlmostEqual(divComplex(-1 + -3j, -5 + -1j), (0.3076923076923077+0.5384615384615384j), "Test failed on all negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_one(self):
        self.assertEqual(divComplex(-20 + 12j, -13 + -16j), (0.16-1.12j), "Test failed on mixed positive and negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_two(self):
        self.assertEqual(divComplex(-20 + -12j, 13 + -16j), (-0.16-1.12j), "Test failed on mixed positive and negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_three(self):
        self.assertEqual(divComplex(20 + -12j, 13 + 16j), (0.16-1.12j), "Test failed on mixed positive and negative")
    #Test num1 positive and num2 negative.
    def test_num1_positive_num2_negative(self):
        self.assertAlmostEqual(divComplex(20 + 12j, -13 + -16j), (-1.0635294117647058+0.38588235294117645j), "Test failed on num1 positive and num2 negative")
    #Test num1 negative and num2 positive.
    def test_num1_negative_num2_positive(self):
        self.assertAlmostEqual(divComplex(-20 + -12j, 13 + 16j), (-1.0635294117647058+0.38588235294117645j), "Test failed on num1 negative and num2 positive")
    #Test only real.
    def test_only_real(self):
        self.assertEqual(divComplex(1, 2), 0.5, "Test failed only real")
    #Test only imaginary.
    def test_only_imaginary(self):
        self.assertEqual(divComplex(1j, 2j), (0.5+0j), "Test failed only imaginary")
    #Test one real one imaginary.
    def test_one_real_one_imaginary(self):
        self.assertEqual(divComplex(1, 2j), (-0.5j), "Test failed on one real one imaginary")
    #Test one imaginary one real.
    def test_one_imaginary_one_real(self):
        self.assertEqual(divComplex(1j, 2), (0.5j), "Test failed on one imaginary one real")
    #Test num1 and -(num1).
    def test_num1_negated_num1(self):
        self.assertEqual(divComplex(7 + -6j, -7 + 6j),-1-0j, "Test failed on num1 and -(num1)")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_one(self):
        self.assertAlmostEqual(divComplex(-.2 + 1.2j, -1.3 + -1.6j), (-0.39058823529411757-0.4423529411764706j), 7, "Test failed on mixed positive and negative decimals")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_two(self):
        self.assertAlmostEqual(divComplex(-20.35 + -12.12j, 13.3 + -16.7j), (-0.14974549124577663-1.0993044890078547j), 7, "Test failed on mixed positive and negative decimals")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_three(self):
        self.assertAlmostEqual(divComplex(3.14159 + -12.6j, -3.14159 + 16j), -0.7953884065309722-0.04017535849539769j, 7, "Test failed on mixed positive and negative decimals")
    def test_all_one(self):
        self.assertTrue(divComplex(1 + 1j,1 + 1j) == 1,"Test failed when every number is 1")
    def test_zero_over_num2(self):
        self.assertTrue(divComplex(0,10) == 0, "Test failed when 0/number")
    def test_nan1(self):
        self.assertTrue(cmath.isnan(divComplex(0j,0j)), "Test failed when number/0, did not return NaN")
    def test_nan2(self):
        self.assertTrue(cmath.isnan(divComplex(1,0)), "Test failed when number/0, did not return NaN")
    def test_nan3(self):
        self.assertTrue(cmath.isnan(divComplex(0j,0j +0)), "Test failed when number/0, did not return NaN")

"""
This class is a test class used to test the modComplex fuction.

Example:

print(((modComplex(-3+4j) == 5))

Output
----------------------
True

"""
class modComplexTest(unittest.TestCase):

    def test_zero_real(self):
        self.assertTrue((modComplex(0) == 0), "Test failed when 0 is given")
    def test_zer_imag(self):
        self.assertTrue((modComplex(0j) == 0), "Test failed when 0j is given ")
    def test_onereal_oneimaginary(self):
        self.assertTrue(isclose(modComplex(1+1j),1.4142135623730951), "Test failed when 1+1i is given")
    def test_negitive_postive(self):
        self.assertTrue((modComplex(-3+4j) == 5), "Test failed when -3+4j is given Note: answer is always postive")
    def test_zero_imag(self):
        self.assertTrue((modComplex(12+0j)== 12), "Test failed when imag is 0 ")
    def test_zero_real(self):
        self.assertTrue((modComplex(0+6j) == 6), "Test failed when real is 0")
    def test_decimal_negImag(self):
        self.assertTrue((isclose(modComplex(12.5 - 5.33j),13.588925638180527)), "Test failed when both numbers are decimal and imaginary is negative")
    def test_both_negative(self):
        self.assertTrue((isclose(modComplex(-5-5j), 7.0710678118654755)), "Test failed when both negative ")
    def test_decimal(self):
        self.assertTrue((isclose(modComplex(-14.66 + 2.25j), 14.831658706968685)), "Test failed when -14.66 + 2.25j given")

"""
This class is a test class used to test the conjComplex fuction.

Example:


print(conjComplex(3 + 2j) == 3 - 2j)

Output
----------------------
True

"""
class conjComplexTest(unittest.TestCase):
    def test_pos_pos(self):
        self.assertTrue(conjComplex(3 + 2j) == 3 - 2j , "Test failed when both positive")
    def test_zero(self):
        self.assertTrue(conjComplex(0) == 0 , "Test failed when 0 is given ")
    def test_real(self):
        self.assertTrue(conjComplex(5) == 5 , "Test failed when only pos real is given")
    def test_imag(self):
        self.assertTrue(conjComplex(5j) == -5j , "Test failed when pos imag is given ")
    def test_all_neg(self):
        self.assertTrue(conjComplex(-5 + -6j) == -5 + 6j , "Test failed when both negative")
    def test_zeroimag(self):
        self.assertTrue(conjComplex(0j) == 0 , "Test failed when zero imaginary is given ")
    def test_neg_pos(self):
        self.assertTrue(conjComplex(-3 - -8j)== -3 - 8j , "Test failed when negative real and positive imag")
    def test_zero_zero(self):
        self.assertTrue(conjComplex(0 + 0j) == 0 , "Test failed on 0 + 0j ")


def testDivComplex():
    divComplexTests = unittest.TestLoader().loadTestsFromTestCase(divComplexTest)
    unittest.TextTestRunner(verbosity=1).run(divComplexTests)
def testModComplex():
    modComplexTests = unittest.TestLoader().loadTestsFromTestCase(modComplexTest)
    unittest.TextTestRunner(verbosity=1).run(modComplexTests)
def testConjComplex():
    conjComplexTests = unittest.TestLoader().loadTestsFromTestCase(conjComplexTest)
    unittest.TextTestRunner(verbosity=1).run(conjComplexTests)

def runtests():
    testDivComplex()
    testModComplex()
    testConjComplex()
