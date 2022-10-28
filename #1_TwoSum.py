import random

#---Asking for a list limit---

print('Enter the leanth of the array/list:- ',end='')
len_list = int(input())


#---Randomly generating a list and a target---

nums = [random.randint(1,len_list) for x in range(len_list+1)]
target = random.randint(2,len_list)


#---Showing the list and the target---

print(nums)
print(target)


#---Linearly finding the answer---

for i,e in enumerate(nums):
    f = target - e
    if f in nums[:i:]:
        print(f"[{nums.index(f)},{i}] [{f} + {e} = {target}]\n")