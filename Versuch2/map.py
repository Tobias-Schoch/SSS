import random

# -------- dead -------- #
a = 75
b = 25
rand = 0

aa = 0
bb = 0

for x in range(0, 2000):
    rand = random.randint(1, a + b)
    if (rand >= a):
        aa += 1
    if(rand < a):
        bb += 1

print("A " + str(aa))
print("B " + str(bb))