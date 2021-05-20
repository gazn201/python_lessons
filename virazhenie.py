a, b, c = map(int, input().split())
var1 = a+b*c
var2 = a*b+c
var3 = (a+b)*c
var4 = a*(b+c)
var5 = a*b*c
print(max(var1, var2, var3,var4, var5))
