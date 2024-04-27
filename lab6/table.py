class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):

        print("V:",((let_num(key[0]) - 1) * 33 + (let_num(key[1]) - 1)))
        print("Hash:",((let_num(key[0])-1) * 33 + (let_num(key[1])-1)) % self.size)
        return ((let_num(key[0])-1) * 33 + (let_num(key[1])-1)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size


def let_num(let):
    let = let.lower()
    if let == 'ё':
        return let_num('е') + 1
    return ord(let) - ord('а') + 1 + (ord(let) > (ord('е')))

