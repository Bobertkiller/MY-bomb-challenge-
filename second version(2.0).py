import random

f1 = ["ap1", "ap2", "ap3", "ap4"]
f2 = ["ap5", "ap6", "ap7", "ap8"]
f3 = ["ap9", "ap10", "ap11", "ap12"]
f4 = ["ap13", "ap14", "ap15", "ap16"]

building = [f1 , f2, f3, f4]
bombs = []

bq = int(input("How many bombs do you desire? "))
print("please answer the following with yes or no")
twoin1 = str(input("Do you want more then one bomb in an apartment? "))

twoin1 =twoin1.lower()
#I made it possible for the user to choose how many bombs he wants to be generated, and if he wants
#to have the possibility for there to be more then one bomb in an apartment
g = 1

for g in range(bq):
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    bl = building[a][b]
    bombs.append(bl)
        # I was testing with lists , then had to make a dictionary to remove duplicates,
        # but for the next version i will use SETS
reroll = []
if twoin1 == "no":
    bombs2 = set(dict.fromkeys(bombs))
    size = len(bombs2)
    while size != bq:
        r = bq - size
        for g in range(r):
            c = random.randint(0, 3)
            d = random.randint(0, 3)
            bl2 = building[c][d]
            reroll.append(bl2)
            reroll2 = set(reroll)
            size2 = len(reroll2)
            sf = len(reroll2.intersection(bombs2))
            print(reroll, r, bq, size, sf)
            if sf >= 1:
                reroll.clear()
            if size2 == r and sf == 0:
                bombsf = bombs2.union(reroll2)
                break
        else:
            continue
        break
else:pass
#I was able to make this verification to work, thus my code can be true to the bomb quantity that is randomly generated, now i need to make the floor verification
#and make it so the user determines how many bombs will be generated
exit() #I will now star to program the next section of my challenge and i will upload it as a 3.0
#I put this exit() to do some testing so please ignore what comes in the next blocks of code since i am testing a way
# to generate random bombs and avoid duplicates
#After achieving this i will make thhe user input so you may choose how many bombs you want, and use a bollean to
# change the rules of my code to permit multiple bombs in the same apartment
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
