from TestCase import TestCase

class WasRun(TestCase):
    
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.WasRun = None



    def test_method(self):
        self.WasRun = 1


if __name__ == "__main__":
    test= WasRun("test_method")
    print(test.WasRun)
    # test.test_method()
    test.run()
    print(test.WasRun)
