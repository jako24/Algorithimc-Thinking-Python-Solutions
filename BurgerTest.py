import unittest
from Burger import burger_max

class TestMaxBurger(unittest.TestCase):
    
    def test_case_1(self):
        m, n, t = 4, 9, 15
        self.assertEqual(burger_max(m, n, t), (3,3)) # Homer eats 3 burgers of type m in 12 minutes and has 3 minutes left 
        
    def test_case_2(self):
        m, n, t = 2, 5, 17
        self.assertEqual(burger_max(m, n, t), (8, 1)) # Homer eats 8 burgers of type m in 16 minutes and has 1 minute left 
    
    def test_case_3(self):
        m,n,t = 4, 6, 24
        self.assertEqual(burger_max(m,n,t), (6, 0))
        
    def test_case_4(self):
        m, n, t = 5, 8, 12
        self.assertEqual(burger_max(m,n,t), (2,2))
        
if __name__ == '__main__':
    unittest.main()