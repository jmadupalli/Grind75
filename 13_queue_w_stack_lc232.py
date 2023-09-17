# https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    # two ways we can do this, one change the order
    # by shifting all elements, and popping to second stack
    # push the new element, or pop the element
    # and shift back to stack 1, essentially making LIFO, a FIFO
    def pop(self) -> int:
        while self.st1:
            self.st2.append(self.st1.pop())
        e = self.st2.pop()

        while self.st2:
            self.st1.append(self.st2.pop())
        return e

    def peek(self) -> int:
        return self.st1[0]

    def empty(self) -> bool:
        return not self.st1
