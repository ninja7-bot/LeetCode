class NumberContainers:
    def __init__(self):
        self.index_map = {} # index -> num
        self.nums_map = defaultdict(set) # num -> set(indices)

    def change(self, index, number): # parameters: index and number
        """
        1. Check if the index is in index_map. Meaning, if the index is mapped to some number already.
        2. Retrieve the old_number which the index is mapped to.
        3. *IF* old_number == number then just add the index to the number's set.
        4. *ELSE*: remove the old_number from the index.
        5. Insert the new number to that index.
        6. Discard the index from nums_map.
        7. Create a new entry for the new number in the nums_map.
        """

        if index in self.index_map:
            old_num = self.index_map[index]
            
            if old_num == number:
                return
            
            self.nums_map[old_num].discard(index)
            if not self.nums_map[old_num]:
                del self.nums_map[old_num]
                
        self.index_map[index] = number
        self.nums_map[number].add(index)

    def find(self, number):
        """
        1. Check if the number is in nums_map. Meaning, the number is indexed to at least one index.
        2. ALSO, check if the nums_map has a set for the number.
        3. Retrieve that set.
        4. Return the smallest value from that set OR -1.
        """
        if number in self.nums_map and self.nums_map[number]:
            return min(self.nums_map[number])
        return -1


class NumberContainers:

    def __init__(self):
        self.index_map = {} # index -> num
        self.nums_map = defaultdict(list) # num -> heap(indices)

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_num = self.index_map[index]
            if old_num != number:
                heapq.heappush(self.nums_map[old_num], index)
                
        self.index_map[index] = number
        heapq.heappush(self.nums_map[number], index)

    def find(self, number: int) -> int:
        if number not in self.nums_map:
            return -1
        while self.nums_map[number] and self.index_map[self.nums_map[number][0]] != number:
            heapq.heappop(self.nums_map[number])

        return self.nums_map[number][0] if self.nums_map[number] else -1
