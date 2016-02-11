def moveZeroes(nums):
    i = 0
    for count in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            i-=1
        count+=1
        i+=1
    return nums

print moveZeroes([2,3,3,0,0,8,0,2,0,9,3,0])
