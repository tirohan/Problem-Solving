#for loops partial dive

list1= [['rohan', 2], ['rodela', 4], ['nijhum', 7], ['sahana', 9 ]]

dict1= dict(list1)

for item in dict1:
    print(item)
    break
for item, orange in dict1.items():
    print(item, orange)
