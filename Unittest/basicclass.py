import unittest

class PythonClassTests(unittest.TestCase):
    pass

class PythonClass(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

if __name__ == "__main__":
    unittest.main()