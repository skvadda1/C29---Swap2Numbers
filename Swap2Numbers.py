def swap1(a,b):
    a = a^b
    b = a^b
    a = a^b
    print("After Swapping:\n a =", a,"\n b =",b)
def swap2(a,b):
    a = (a&b)+(a|b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("After Swapping:\n a =", a,"\n b =",b)
swap1(10,20)
swap2(10,20)
