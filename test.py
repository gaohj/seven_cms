num = 123
d = {'age':12}

def change(num,d):
    num -=1
    d['age'] -= 1

change(num,d)
print(num,d['age'])