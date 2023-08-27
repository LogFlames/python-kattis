input()
n = [*map(int, input().split())]
nums = {}
for nn in n:
    if nn not in nums:
        nums[nn] = 0
    nums[nn] += 1

ns = sorted(nums.keys())
c = 0
t = 0
for i in range(len(ns)):
    if i > 0 and ns[i] - ns[i - 1] > 1:
        c = 0
    if nums[ns[i]] > c:
        t += nums[ns[i]] - c
    c = nums[ns[i]]
print(t)
