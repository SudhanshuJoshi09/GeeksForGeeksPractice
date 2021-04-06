class FibValue:

    def __init__(self):
        self.val_list = [0, 1]

    def fib_value(self, n):
        if n < len(self.val_list):
            self.val_list[n]
        
        for i in range(len(self.val_list) - 1, n+1):
            temp_a = self.val_list[i]
            temp_b = self.val_list[i-1]

            self.val_list.append(temp_a + temp_b)
        
        return self.val_list[n]

if __name__ == '__main__':
    f = FibValue()
    v1 = f.fib_value(i)
    print(v1, end = ' ')