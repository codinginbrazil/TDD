from TestCase import TestCase

from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):
    
    def testRunning(self):
        test= WasRun("testMethod")
        assert(not test.wasRun)
        
        test.run()
        assert(test.wasRun)
        
        TestCaseTest("testRunning").run()


    def setUp(self):
        self.result= TestResult()


    def testSetUp(self):
        self.test.run()
        # assert(self.test.wasSetUp)
        assert("setUp testMethod " == self.test.log)

    def testTemplateMethod(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

        
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
        
        
    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
        
        
    def testResult(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())
        
        
    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())


    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())
        
        
    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())
