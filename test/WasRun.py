from TestCase import TestCase

class WasRun(TestCase):
    
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.WasRun = None


    def test_method(self):
        self.log= self.log + "testMethod "

        
    def setUp(self):
        self.log = "setUp "
        

    def tearDown(self):
        self.log= self.log + "tearDown "


if __name__ == "__main__":
    test= WasRun("test_method")
    print(test.WasRun)
    
    # test.run()
    print(test.WasRun)
