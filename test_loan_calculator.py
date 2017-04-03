import unittest
from loan_calculator import loan_function

class LoanCalculator(unittest.TestCase):
	def test_it_works(self):
		self.assertEquals(loan_function(100000,12,12), 112000,"Some Error")

if __name__ =="__main__":
	unittest.main()