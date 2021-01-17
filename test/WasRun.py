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
        
        
    def testBrokenMethod(self):
        raise Exception
