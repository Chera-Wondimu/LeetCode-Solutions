class Solution:
    def canAliceWin(self, n: int) -> bool:
        move = 10
        turns = 0
        while n >= move:
            n -= move
            move -= 1
            turns += 1
        return turns % 2 == 1
