import unittest
import module_12_1
import module_12_2

M_test = unittest.TestSuite()
M_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
M_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(M_test)
