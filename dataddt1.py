from ddt import ddt,data,unpack
import unittest

@ddt
class mytesting (unittest.TestCase):
  def setup (self):
    print ("this is the setup")

  @data ([1,2,3])
  # @unpack
  def test_1 (self, value):
    print (value)
      
  # @data([3, 2, 1], [5, 3, 2], [10, 5, 6])
  # @unpack
  # def test_minus(self, a, b, expected):
  #     actual = int(a) - int(b)
  #     expected = int(expected)
  #     # self.assertequal(actual, expected)
  #     self.assertEqual(actual,expected)
  #
  # @data([2,3], [4,5])
  # def test_compare (self, a, b):
  #   self.assertEqual (a, b)

  def teardown (self):
    print ("this is teardown")

if __name__ == "__main__":
    unittest.main (verbosity=2)

# test_minus()