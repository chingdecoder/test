lst=[]
for i in range(6):
    lst+=input()
print(str(max(lst)),(max(y for y in lst if y!=max(lst)) ) )