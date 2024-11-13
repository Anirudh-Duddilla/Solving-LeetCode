class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1 and flowerbed[0] == 0:
            if n == 0 or n == 1: return True
            elif n>1:return False
        for i in range(length):
            # print(i,n)
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == length-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -=1
            elif flowerbed[i-1] ==0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        if n > 0:
            return False
        return True