from TestResult import TestResult

class TestSuite(object):
   
    def __init__(self):
        self.tests= []
    
    
    def add(self, test):
        self.tests.append(test)
        
        
    def run(self):
        result = TestResult()
        for test in tests:
            test.run(result)

