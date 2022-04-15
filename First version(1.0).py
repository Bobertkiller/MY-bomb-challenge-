import random

f1 = ["ap1", "ap2", "ap3", "ap4"]
f2 = ["ap5", "ap6", "ap7", "ap8"]
f3 = ["ap9", "ap10", "ap11", "ap12"]
f4 = ["ap13", "ap14", "ap15", "ap16"]

building = [f1 , f2, f3, f4]
bombs = [] 

bq = random.randint(1,10)
g = 1
size = len(bombs)

for g in range(bq):
    a = random.randint(0,3)
    b = random.randint(0,3)
    bl = building[a][b]
    bombs.append(bl)
    a = a + 1
    b = b + 1
    if a > 3:
        a = 0
    if b > 3:
        b = 0
    bombs = list(dict.fromkeys(bombs))#I was testing with lists , then had to make a dictionary to remove duplicates, but for the next version i will use SETS
    print(bl, a, b, bq)
print(bombs)
exit()
#I put this exit() to do some testing so please ignore what comes in the next blocks of code since i am testing a way to generate random bombs and avoid duplicates
#After achieving this i will make thhe user input so you may choose how many bombs you want, and use a bollean to change the rules of my code to permit multiple bombs in the same apartment
bf1 = random.randint(0, 3)#bomb flor
bomb1 = random.randint(0, 3)

bf2 = random.randint(0, 3)#bomb flor
bomb2 = random.randint(0, 3)

if bf2 == bf1:
    pass
if bomb2 == bomb1:
    pass

bl1 = building[bf1][bomb1] #bomb location

bl2 = building[bf2][bomb2]

for i in range(4):
    x = building[i]
    for i in range(4):
        y = x[i]
        if y == bl1 or y == bl2:
            pass
        else:print(y, "Apartment CLEARED")
        if y == bl1:
            print(f"A bomb has been located at {bl1} STAND CLEAR!!!!!")
        if y == bl2:
            print(f"A bomb has been located at {bl2} STAND CLEAR!!!!!")
