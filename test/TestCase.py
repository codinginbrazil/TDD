from TestResult import TestResult

class TestCase(object):
    def __init__(self, name):
        self.name = name
        
    def setUp(self):
        pass
    
    
    # def run(self, result):
    #     result.testStarted()
    #     self.setUp()
    #     method = getattr(self, self.name)
    #     method()
    #     self.tearDown()
        
    def run(self):
        result= TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

        
    def tearDown(self):
        pass



