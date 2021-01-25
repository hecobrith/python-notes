import json 
from random import sample

class PythonClass(object):
    def __init__(self, name='default name', items=None):
        self.name = name
        self.items = items 

    def get_name(self):
        return f'name is {self.name}'

    def get_items(self):
        return 'items are {self.items}'
    
    def get_name_items_dict(self):
        return dict(name = self.name,
                    items = self.items)
    
twenty_nums = sample(range(100), 20)
data_list = PythonClass('data_list', twenty_nums)

print(data_list.get_name())
print(data_list.get_items())
print(data_list.get_name_items_dict())

with open('twenty_nums.json', 'w') as json_file:
    json.dump(data_list.get_name_items_dict(), json_file, indent=2)
    print(json_file)

with open('twenty_nums.json', 'r') as json_file:
    some_data = json.load(json_file)

print(some_data)
print(some_data.keys())
print(some_data['items'])
print(type(some_data))
