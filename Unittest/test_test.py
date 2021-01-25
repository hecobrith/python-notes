import unittest

class PythonClassTests(unittest.TestCase):
    # All test comes with a setup module
    def setUp(self):
        self.name = 'bob'
        self.inst = PythonClass(self.name)

    # automaticly will run test case with word test_
    def test_(self):
        print("hello")
    
    def test_exeption(self):
        self.assertRaises(TypeError, PythonClass)

    def test_name(self):
        ''' we dont need to declare and instanciate cos of setup module
        name = 'bob'
        inst = PythonClass(name)
        '''
        name_returned = self.inst.get_name()
        # assert equal will commpare values
        self.assertEqual(self.name, name_returned)

    def test_name_wrong(self):
        name_returned = self.inst.get_name()
        name_wrong = 'bill'
        self.assertNotEqual(name_wrong, name_returned)

class PythonClass(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

if __name__ == "__main__":
    unittest.main()