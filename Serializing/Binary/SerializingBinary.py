import pickle

class PythonClass(object):
    def __init__(self, name='default name', items=None):
        self.name = name
        self.items = items
        print('*** init self__dict__', self.__dict__)
        for item in self.items:
            print(f'item in init: {item}')

    def get_name(self):
        return self.name

    # invoked during pickling
    def __getstate__(self):
        print('self.__dict__ in __getstate__', self.__dict__)
        return self.__dict__.copy()

    # invoked during unppickling
    def __setstate__(self, state):
        print('\nself.__dict__ in __setstate__ before updating stating***')
        print(self.__dict__)
        self.__dict__.update(state)
        print('self.__dict__ in __setstate__ after updating state***')
        print(self.__dict__)
        for item in self.items:
            print(f'item in __setstate__: {item}')    

some_items = [1, 2]
bob = PythonClass(name='Bob', items=some_items)
print('Bob before:', bob.get_name())

# open a file to write raw binary and pickle the class object
with open('bob','wb') as bob_file:
    pickle.dump(bob, bob_file)

#
with open('bob','rb') as unpickle_bob_file:
    bob_unpickle = pickle.load(unpickle_bob_file)

print('Bob after:', bob_unpickle.get_name())