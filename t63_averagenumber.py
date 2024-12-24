def avenum(nums):
    nums=list(map(int,nums.split()))
    nums.pop()
    return 'Incorrect input' if len(nums)==0 else sum(nums)/len(nums)


print(avenum(input()))