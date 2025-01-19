import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_walk(self):
        tester1 = runner.Runner("Kaneki")
        for i in range(10):
            tester1.walk()
        self.assertEqual(tester1.distance, 50)

    def test_run(self):
        tester2 = runner.Runner('Gas')
        for i in range(10):
            tester2.run()
        self.assertEqual(tester2.distance, 100)

    def test_challenge(self):
        tester1 = runner.Runner('Kira')
        tester2 = runner.Runner("L")
        for i in range(10):
            tester1.walk()
            tester2.run()
        self.assertNotEqual(tester2.distance, tester1.distance)
