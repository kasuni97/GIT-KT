roll_no = [1,2,3,4,5]
names = ["Kasuni", "Sam","Ann", "Sony", "Danny"]
mix_list= [1, "ann", True, 1010]
print(roll_no)
print(roll_no[0])
print(roll_no[1])
print(names[2])
print(len(names))
print(mix_list[-1])
print(roll_no[0:2])
print(roll_no[0:5:2])
roll_no.sort()
print(roll_no)
roll_no.reverse()
print(roll_no)
print(min(roll_no))
print(max(roll_no))
roll_no.append(10) #add elements
print(roll_no)
roll_no.insert(2,"Sam")
print(roll_no)
roll_no.pop() #remove the last element
print(roll_no)
roll_no.pop(2) #index 2 element removed
print(roll_no)
roll_no.extend([8,6,8,3])
print(roll_no)
