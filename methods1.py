def isMetro(city):
    l = ['sfo', 'nyc', 'la']
    if city in l:
        return True
    else:
        return False
x = isMetro('sfo')
print("the value entered is sfo that is why result is:" + str(x))
