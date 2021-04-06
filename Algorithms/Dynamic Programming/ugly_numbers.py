#User function Template for python3
import sys


class Solution:
    
    def __init__(self):
        self.val_list = [1]
    
    def get_min(self, *args):
        total_val = list(args)
        val = sys.maxsize
        for i in range(len(total_val)):
            if total_val[i] < val:
                val = total_val[i]
    
        return val

    def getNthUglyNo(self, n):
        a = 2
        b = 3
        c = 5
        a_idx = 0
        b_idx = 0
        c_idx = 0
    
        if n < len(self.val_list):
            return self.val_list[n-1]
            
        for i in range(len(self.val_list), n):
            a_temp = self.val_list[a_idx]*a
            b_temp = self.val_list[b_idx]*b
            c_temp = self.val_list[c_idx]*c
    
            min_val = self.get_min(a_temp, b_temp, c_temp)
    
            if min_val == a_temp:
                a_idx += 1
            if min_val == b_temp:
                b_idx += 1
            if min_val == c_temp:
                c_idx += 1
            
            self.val_list.append(min_val)
    
        return (self.val_list[n-1])


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1