
l1 = [2,4,3]
l2 = [5,6,4]
itog = ""
itog2 = ""

for i in l1:
    i = str(i)
    itog = itog + i

for a in l2:
    a = str(a)
    itog2 = itog2 + a


itog = int(itog)
itog2 = int(itog2)
sum = itog + itog2
sum = str(sum)
print(sum[: :-1])




