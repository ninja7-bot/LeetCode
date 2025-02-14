class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)
    
    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k-1]


pon = ProductOfNumbers()
nums = [3,0,2,5,4]
for num in nums:
    pon.add(num)

pon.getProduct(3)
