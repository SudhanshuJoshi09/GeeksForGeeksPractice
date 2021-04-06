c = [1]
def catalan_num(n):
    if n < len(c):
        return c[n]
    
    c_n = 1
    for i in range(2, n+1):
        c_n = (n + i)

    for i in range(2, n+1):
        c_n //= i
        
    return c_n
