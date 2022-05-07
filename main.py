# Task1: recursive function

def power(a, b):
    if a < 0 or b < 0:
        return -1
    # base case
    if b == 0:
        return 1
    # recursive relation
    else:
        return a * power(a, b - 1)


# test
a: int = 5
b: int = 3

print(power(a, b))


# Task2:BinarySearch (py3 for recursive bs) returns index of x in arr if present, else -1

def binary_search(numbers, num, start, end):
    # check base case
    if end >= start:
        mid = (end + start) // 2
        # if element is present at the middle itself
        if numbers[mid] == num:
            return mid

        elif numbers[mid] > num:
            return binary_search(numbers, num, start, mid - 1)  # If element is smaller than mid, then - in left part

        else:
            return binary_search(numbers, num, mid + 1, end)  # Else the element can be only in right part
    else:
        return -1  # when element is not present at all


numbers = [1, 3, 5, 7, 9, 11, 15, 17]
start = 0
end = 7
print(binary_search(numbers, 7, start, end))


# Task3:HashTable
class HashTable:
    # constructor
    def __init__(self, size):
        self.size = size
        self.data_list = []
        for x in range(self.size):
            self.data_list.append([])

    # __str__ function for printing all the members of a class HT
    def __repr__(self):
        return self.data_list.__repr__()

    # Task4: creating hash function based on length of string / value of int
    def ___my__hash(self, element):
        # check if element is of type string
        if type(element) is str:
            return len(element) % self.size
        # check if element is of type int
        elif type(element) is int:
            return element % self.size

    # Task5: Implementation(insert(self,element))
    def insert(self, element):
        # append element to the hashbucket with the hashkey computed by __my__hash-function
        self.data_list[self.___my__hash(element)].append(element)

    # Task6: Implementation(get_element(self, element))
    def get_element(self, element):
        hash_bucket_key = self.___my__hash(element)
        for el in self.data_list[hash_bucket_key]:
            # remove the element and return it
            if el == element:
                self.data_list[hash_bucket_key].remove(el)
                return el
        return False

    # Task7:Implementation(get_size(self))
    def get_size(self):
        count = 0
        # return the number of used hashbuckets
        for hash_bucket in self.data_list:
            if len(hash_bucket) > 0:
                count += 1
        return count


ht = HashTable(10)
ht.insert("Sirena")
ht.insert("Unicorn")
ht.insert("Pegasus")
ht.insert("Elf")
ht.insert("Aralez")
ht.insert(10)
ht.insert(15)
ht.insert(11)
ht.insert(17)
print(ht)

print(ht.get_element("Hobbit"))
print(ht.get_element("Aralez"))
print(ht)
print(ht.get_size())
print(ht.get_element(10))
print(ht.get_size())
print(ht)

