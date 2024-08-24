import random

class RandomizedSet:

    def __init__(self):
       self.list_container = [] 
       self.num_elements = 0
       self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False

        self.list_container.append(val)
        self.num_elements += 1
        self.hashmap[val] = self.num_elements - 1    

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False

        self.list_container.remove(val)
        self.num_elements -= 1    
        self.hashmap.pop(val)
        return True

    def getRandom(self) -> int:
        random_int = random.randint(0,self.num_elements - 1)
        return random.choice(self.list_container)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()