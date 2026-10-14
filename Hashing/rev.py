"""
Q4. First Non-Repeating Character 🔥

Difficulty: Medium

Given:

s = "aabbcdde"

Find the first character that appears exactly once.

Expected output:

c

Explanation:

Character	Frequency
a	2
b	2
c	1
d	2
e	1

Although both c and e appear once, c comes first in the original string.

Rules:

Use a dictionary to calculate frequencies.
Preserve the original string order when searching.
Don't use Counter or sorting.

Concept: Frequency hashing and maintaining original order.

Q5. Two Sum — Classic Placement Interview Problem 🚀

Difficulty: Medium–Hard

Given an array of integers and a target, find the indices of two distinct elements whose sum equals the target.

Example:

nums = [2, 7, 11, 15]
target = 9

Expected output:

[0, 1]

Because:

nums[0] + nums[1] = 2 + 7 = 9

Another example:

nums = [3, 2, 4]
target = 6

Expected output:

[1, 2]

Rules:

Use a dictionary.
Don't use nested loops.
Aim for O(N) time complexity.
Return indices, not the two numbers.

Interview hint: Think about this equation:

$$ \text{Required number} = \text{target} - \text{current number} $$

Can a dictionary help you check whether the required number has already appeared?
"""

arr = [5, 2, 5, 3, 2, 5, 4, 2]
hmp={}
for i in arr:
    hmp[i]=hmp.get(i,0)+1
highest_freq=0
ans=0
for num in hmp:
    if highest_freq<hmp[num]:
        highest_freq=hmp[num]
ans=float('inf')
for n in hmp:
    if hmp[n]==highest_freq and n<ans:
        ans=n
print(ans)