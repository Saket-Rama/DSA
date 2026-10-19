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
"""
n=input()
st="abacdae"
hmp={}
for i in st:
    hmp[i]=hmp.get(i,0)+1
print(hmp.get(n,0))