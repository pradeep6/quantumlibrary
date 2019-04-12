import unittest

"""
This class is a test class used to test the getReal fuction.

Example:

num1 = 10 + 12j
print(getReal(num1) == 10)

Output
----------------------
True

"""
class getRealTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_positive_real(self):
        self.assertEqual(getReal(1) , 1, "Test failed on positive real")
    #Test negative real zero imaginary.
    def test_negative_real(self):
        self.assertEqual(getReal(-2) , -2, "Test failed on negative real")
    #Test positive real and positive imaginary.
    def test_positive_real_positive_imaginary(self):
        self.assertEqual(getReal(3 + 4j) , 3, "Test failed on positive real and positive imaginary")
    #Test negative real and positive imaginary.
    def test_negative_real_positive_imaginary(self):
        self.assertEqual(getReal(-4 + 5j) , -4, "Test failed on negative real and positive imaginary")
    #Test positive real and negative imaginary.
    def test_positive_real_negative_imaginary(self):
        self.assertEqual(getReal(5 + -6j) , 5, "Test failed on positive real and negative imaginary")
    #Test negative real and negative imaginary.
    def test_negative_real_negative_imaginary(self):
        self.assertEqual(getReal(-6 + -7j) , -6, "Test failed on negative real and negative imaginary")
    #Test zero real and positive imaginary.
    def test_positive_imaginary(self):
        self.assertEqual(getReal(7j) , 0, "Test failed positive imaginary")
    #Test zero real and negative imaginary.
    def test_negative_imaginary(self):
        self.assertEqual(getReal(-7j) , 0, "Test failed negative imaginary")
    #Test zero real and positive imaginary.
    def test_zero(self):
        self.assertEqual(getReal(0) , 0, "Test failed on zero")
    #Test decimal real and decimal imaginary.
    def test_decimal_real_decimal_imaginary(self):
        self.assertEqual(getReal(8.9 + 9.10j) , 8.9, "Test failed on decimal real and decimal imaginary")
    #Test decimal real.
    def test_decimal_real(self):
        self.assertEqual(getReal(9.10) , 9.10, "Test failed on decimal real")
    #Test decimal imaginary.
    def test_decimal_imaginary(self):
        self.assertEqual(getReal(9.10j) , 0, "Test failed on decimal imaginary")
"""
This class is a test class used to test the getImaginary fuction.

Example:

num1 = 10 + 12j
print(getImaginary(num1) == 12)

Output
----------------------
True

"""
class getImaginaryTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_positive_real(self):
        self.assertEqual(getImaginary(1) , 0, "Test failed on positive real")
    #Test negative real zero imaginary.
    def test_negative_real(self):
        self.assertEqual(getImaginary(-2) , 0, "Test failed on negative real")
    #Test positive real and positive imaginary.
    def test_positive_real_positive_imaginary(self):
        self.assertEqual(getImaginary(3 + 4j) , 4, "Test failed on positive real and positive imaginary")
    #Test negative real and positive imaginary.
    def test_negative_real_positive_imaginary(self):
        self.assertEqual(getImaginary(-4 + 5j) , 5, "Test failed on negative real and positive imaginary")
    #Test positive real and negative imaginary.
    def test_positive_real_negative_imaginary(self):
        self.assertEqual(getImaginary(5 + -6j) , -6, "Test failed on positive real and negative imaginary")
    #Test negative real and negative imaginary.
    def test_negative_real_negative_imaginary(self):
        self.assertEqual(getImaginary(-6 + -7j) , -7, "Test failed on negative real and negative imaginary")
    #Test zero real and positive imaginary.
    def test_positive_imaginary(self):
        self.assertEqual(getImaginary(7j) , 7, "Test failed positive imaginary")
    #Test zero real and negative imaginary.
    def test_negative_imaginary(self):
        self.assertEqual(getImaginary(-7j) , -7, "Test failed negative imaginary")
    #Test zero real and positive imaginary.
    def test_zero(self):
        self.assertEqual(getImaginary(0) , 0, "Test failed on zero")
    #Test decimal real and decimal imaginary.
    def test_decimal_real_decimal_imaginary(self):
        self.assertEqual(getImaginary(8.9 + 9.10j) , 9.10, "Test failed on decimal real and decimal imaginary")
    #Test decimal real.
    def test_decimal_real(self):
        self.assertEqual(getImaginary(9.10) , 0, "Test failed on decimal real")
    #Test decimal imaginary.
    def test_decimal_imaginary(self):
        self.assertEqual(getImaginary(9.10j) , 9.10, "Test failed on decimal imaginary")


"""
This class is a test class used to test the sumComplex fuction.

Example:

num1 = 10 + 12j
num2 = 1 + -2j
print(sumComplex(num1,num2) == 34 + -8j)

Output
----------------------
True

"""
class sumComplexTest(unittest.TestCase):
    #Test all positive.
    def test_positive_all(self):
        self.assertEqual(sumComplex(1 + 2j, 3 + 4j), (4 + 6j), "Test failed on all positive")
    #Test all negative.
    def test_negative_all(self):
        self.assertEqual(sumComplex(-1 + -3j, -5 + -1j), (-6 + -4j), "Test failed on all negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_one(self):
        self.assertEqual(sumComplex(-20 + 12j, -13 + -16j), (-33 - 4j), "Test failed on mixed positive and negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_two(self):
        self.assertEqual(sumComplex(-20 + -12j, 13 + -16j), (-7 - 28j), "Test failed on mixed positive and negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_three(self):
        self.assertEqual(sumComplex(20 + -12j, 13 + 16j), (33 + 4j), "Test failed on mixed positive and negative")
    #Test num1 positive and num2 negative.
    def test_num1_positive_num2_negative(self):
        self.assertEqual(sumComplex(20 + 12j, -13 + -16j), (7 + -4j), "Test failed on num1 positive and num2 negative")
    #Test num1 negative and num2 positive.
    def test_num1_negative_num2_positive(self):
        self.assertEqual(sumComplex(-20 + -12j, 13 + 16j), (-7 + 4j), "Test failed on num1 negative and num2 positive")
    #Test only real.
    def test_only_real(self):
        self.assertEqual(sumComplex(1, 2), 3, "Test failed only real")
    #Test only imaginary.
    def test_only_imaginary(self):
        self.assertEqual(sumComplex(1j, 2j), 3j, "Test failed only imaginary")
    #Test one real one imaginary.
    def test_one_real_one_imaginary(self):
        self.assertEqual(sumComplex(1, 2j), (1 + 2j), "Test failed on one real one imaginary")
    #Test one imaginary one real.
    def test_one_imaginary_one_real(self):
        self.assertEqual(sumComplex(1j, 2), (2 + 1j), "Test failed on one imaginary one real")
    #Test num1 and -(num1).
    def test_num1_negated_num1(self):
        self.assertEqual(sumComplex(7 + -6j, -7 + 6j), 0, "Test failed on num1 and -(num1)")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_one(self):
        self.assertAlmostEqual(sumComplex(-.2 + 1.2j, -1.3 + -1.6j), (-1.5 - .4j), 7, "Test failed on mixed positive and negative decimals")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_two(self):
        self.assertAlmostEqual(sumComplex(-20.35 + -12.12j, 13.3 + -16.7j), (-7.05 - 28.82j), 7, "Test failed on mixed positive and negative decimals")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_three(self):
        self.assertAlmostEqual(sumComplex(3.14159 + -12.6j, -3.14159 + 16j), 3.4j, 7, "Test failed on mixed positive and negative decimals")

"""
This class is a test class used to test the productComplex fuction.

Example:

num1 = 10 + 12j
num2 = 1 + -2j
print(productComplex(num3,num4) == 11 + 10j)

Output
----------------------
True

"""
class productComplexTest(unittest.TestCase):
    #Test all positive.
    def test_positive_all(self):
        self.assertEqual(productComplex(1 + 2j, 3 + 4j), (-5 + 10j), "Test failed on all positive")
    #Test all negative.
    def test_negative_all(self):
        self.assertEqual(productComplex(-1 + -3j, -5 + -1j), (2 + 16j), "Test failed on all negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_one(self):
        self.assertEqual(productComplex(-20 + 12j, -13 + -16j), (452 + 164j), "Test failed on mixed positive and negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_two(self):
        self.assertEqual(productComplex(-20 + -12j, 13 + -16j), (-452 + 164j), "Test failed on mixed positive and negative")
    #Test mixed positive and negative.
    def test_mixed_positive_and_negative_three(self):
        self.assertEqual(productComplex(20 + -12j, 13 + 16j), (452 + 164j), "Test failed on mixed positive and negative")
    #Test num1 positive and num2 negative.
    def test_num1_positive_num2_negative(self):
        self.assertEqual(productComplex(20 + 12j, -13 + -16j), (-68 - 476j), "Test failed on num1 positive and num2 negative")
    #Test num1 negative and num2 positive.
    def test_num1_negative_num2_positive(self):
        self.assertEqual(productComplex(-20 + -12j, 13 + 16j), (-68 - 476j), "Test failed on num1 negative and num2 positive")
    #Test only real.
    def test_only_real(self):
        self.assertEqual(productComplex(1, 2), 2, "Test failed only real")
    #Test only imaginary.
    def test_only_imaginary(self):
        self.assertEqual(productComplex(1j, 2j), -2, "Test failed only imaginary")
    #Test one real one imaginary.
    def test_one_real_one_imaginary(self):
        self.assertEqual(productComplex(1, 2j), 2j, "Test failed on one real one imaginary")
    #Test one imaginary one real.
    def test_one_imaginary_one_real(self):
        self.assertEqual(productComplex(1j, 2), 2j, "Test failed on one imaginary one real")
    #Test num1 and -(num1).
    def test_num1_negated_num1(self):
        self.assertEqual(productComplex(7 + -6j, -7 + 6j), (-13 + 84j), "Test failed on num1 and -(num1)")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_one(self):
        self.assertAlmostEqual(productComplex(-.2 + 1.2j, -1.3 + -1.6j), (2.18 - 1.24j), 7, "Test failed on mixed positive and negative decimals")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_two(self):
        self.assertAlmostEqual(productComplex(-20.35 + -12.12j, 13.3 + -16.7j), (-473.059 + 178.649j), 7, "Test failed on mixed positive and negative decimals")
    #Test mixed positive and negative decimal.
    def test_mixed_positive_and_negative_decimal_three(self):
        self.assertAlmostEqual(productComplex(3.14159 + -12.6j, -3.14159 + 16j), (191.7304122719 + 89.849474j), 7, "Test failed on mixed positive and negative decimals")
    #Test conjugate one.
    def test_conjugate_one(self):
        self.assertEqual(productComplex(3 + -2j, 3 + 2j), 13 , "Test failed on conjugate")
    #Test conjugate two.
    def test_conjugate_two(self):
        self.assertEqual(productComplex(-3 + 2j, 3 + 2j), -13 , "Test failed on conjugate")
    #Test reciprocal one.
    def test_reciprocal_one(self):
        self.assertEqual(productComplex((7 + 4j), ((7/65)-(4j/65))), 1 , "Test failed on reciprocal")
    #Test reciprocal two.
    def test_reciprocal_two(self):
        self.assertEqual(productComplex((-2 - 3j), ((-2/13) + (3j/13))), 1 , "Test failed on reciprocal")

def testGetReal():
    getRealTests = unittest.TestLoader().loadTestsFromTestCase(getRealTest)
    unittest.TextTestRunner(verbosity=1).run(getRealTests)
def testGetImaginary():
    getImaginaryTests = unittest.TestLoader().loadTestsFromTestCase(getImaginaryTest)
    unittest.TextTestRunner(verbosity=1).run(getImaginaryTests)
def testProductComplex():
    productComplexTests = unittest.TestLoader().loadTestsFromTestCase(productComplexTest)
    unittest.TextTestRunner(verbosity=1).run(productComplexTests)
def testSumComplex():
    sumComplexTests = unittest.TestLoader().loadTestsFromTestCase(sumComplexTest)
    unittest.TextTestRunner(verbosity=0).run(sumComplexTests)

def runtests():
    testGetReal()
    testSumComplex()
    testGetImaginary()
    testProductComplex()
    #getImaginaryTests
    #print("test")

    #sumComplex
    #print("test")

    #productComplex
    #print("test")
