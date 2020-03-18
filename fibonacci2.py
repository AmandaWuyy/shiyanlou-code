#!/usr/bin/env python3
a, b = 0, 1
while b < 100:
    print(b, end=' ') # print的另一个参数end，可以将默认的换行符变成空格
    a, b = b, a + b
print() # 换行
