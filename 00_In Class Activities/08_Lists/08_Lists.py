fav_nums = [] #don't need to specifcy how many values are in a list
print(fav_nums)
fav_nums.append(1)
print(fav_nums) #[1]
fav_nums.append(2)
print(fav_nums) #[1,2]
fav_nums.insert(0,5) #1st # specifies location (i.e. beginning of list), 2nd # specifies value
print(fav_nums)
fav_nums += [7,8,9]
print(fav_nums) #[0,1,2,0,7,8,9]
print(fav_nums[4]) #print postiion 4, i.e. 7
print(fav_nums[6]) #print postion 6
print(fav_nums[len(fav_nums)-1]) #print last number in list, "len" finds the length of the list
print(fav_nums[-1]) #print last number in list
print(fav_nums[-2]) #print 2nd to last number in list
removed_num = fav_nums.pop() #takes last number off list
fav_nums.pop(3) #takes 4th value off list
fav_nums[1:1] #"Slicing"
# print range of numbers, last parameter isn't inclusive (from the 2nd value to the 2nd value)
fav_nums[:2] #print from beginning to third value
fav_nums[2:-3] #print nothing, doesn't work
fav_nums[-1:-3] #print nothing, doesn't work