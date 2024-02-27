var=10
def f1():
    global var
    var+=5

def f2():
    f1()
    var=10

f2()
print(var)