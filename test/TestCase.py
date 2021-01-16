class TestCase(object):
    def __init__(self, name):
        self.name= name

    def run(self):
        method = getattr(self, self.name)
        method()

    def testRunning(self):
        test= WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

if __name__ == "__main__":
    TestCaseTest("testRunning").run()
