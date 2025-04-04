class BitwiseOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def bitwise_and(self):
        return self.num1 & self.num2

    def bitwise_or(self):
        return self.num1 | self.num2

    def bitwise_xor(self):
        return self.num1 ^ self.num2

    def bitwise_not(self, num=None):
        if num is None:
            num = self.num1
        return ~num

    def left_shift(self, positions):
        return self.num1 << positions

    def right_shift(self, positions):
        return self.num1 >> positions

