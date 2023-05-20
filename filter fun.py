#The filter()returns an iterator where the items are filtered through a function to test if item is accepted or not
ages=[5,12,17,18,24,32]
def myfunc(x):
    if x>18:
        return True
    else:
        return False
adults=list(filter(myfunc,ages))
for x in adults:
    print(x)

