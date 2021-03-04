'''
- Hash tables store key-value pairs and the key is generated using a hash function.
'''

# Searching
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
my_dict['Dave']
print(my_dict)
# '001'

# Updating
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
my_dict['Dave'] = '004'   #Updating the value of Dave
my_dict['Chris'] = '005'  #adding a key-value pair
print(my_dict)
# {'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}

# Deleting
my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
del my_dict['Dave']  #removes key-value pair of 'Dave'
my_dict.pop('Ava')   #removes the value of 'Ava'
my_dict.popitem()    #removes the last inserted item
print(my_dict)
# {'Joe': '003'}



# Example 1

def hash_key( key, m):
    return key % m


m = 7

print(f'The hash value for 3 is {hash_key(3,m)}')
print(f'The hash value for 2 is {hash_key(2,m)}')
print(f'The hash value for 9 is {hash_key(9,m)}')
print(f'The hash value for 11 is {hash_key(11,m)}')
print(f'The hash value for 7 is {hash_key(7,m)}')

# The hash value for 3 is 3
# The hash value for 2 is 2
# The hash value for 9 is 2
# The hash value for 11 is 4
# The hash value for 7 is 0



# Example 2

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
      
    
t = HashTable()  # this is creating an object
print(t.get_hash('march 6'))
# 9



# example 2

class HashTable2:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for i in range(0, self.size)]
        
    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    
    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        # chaining(closed addressing)
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))
            
    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('does not exist.')
            
    def __setitem__(self, key, value):
        return self.get(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
        
h = HashTable2()

h.set('key1', 'value1')
h.set('key2', 'value2')
h.set('key3', 'value3')
print(h.hashmap)
# [[], [], [('key3', 'value3')], [], [], [], [], [('key1', 'value1'), ('key2', 'value2')], [], []]

h.set(10, 'value1')  # collision will happen here
h.set(20, 'value2')
h.set('key3', 'value3')
print(h.hashmap)
# [[(10, 'value1'), (20, 'value2')], [], [('key3', 'value3')], [], [], [], [], [('key1', 'value1'), ('key2', 'value2')], [], []]