from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test= WasRun("testMethod")
        assert(not test.wasRun)
        
        test.run()
        assert(test.wasRun)
        
        TestCaseTest("testRunning").run()


    def setUp(self):
        self.test = WasRun("testMethod")


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
        test.run()
        assert("setUp testMethod " == test.log)
        
    def testResult(self):
        test= WasRun("testMethod")
        result= test.run()
        assert("1 run, 0 failed" == result.summary())
        
    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        result= test.run()
        assert("1 run, 1 failed", result.summary)

