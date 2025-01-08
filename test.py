nums = list(map(int, input().split()))
target=int(input())
for num in nums:
    rem=target-num
    if ((rem in nums)==True and (nums.index(rem) != nums.index(num))):
        print(nums.index(num))
        print(nums.index(rem))
        break