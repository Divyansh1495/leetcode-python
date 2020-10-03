def reverse(x: int):
        n = 0
        s = 0
        if x < 0:
            s = 1
            x = abs(x)
        while x != 0:
            m = 0
            m = x%10
            n = n*10 + m
            x = int(x/10)
        if s == 1:
            n *= -1
        if n >= -2147483648 and n<= 2147483647:
            return n
        else:
            return 0


print(reverse(-1298434567))