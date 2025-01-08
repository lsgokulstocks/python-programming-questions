---
title: Sample Title
tags: ['sample tag1', 'sample tag2']
---

# Problem Statement

# Solution
```python test.py  -r 'python test.py'
<template>
<sol> 
nums = list(map(int, input().split()))
target=int(input())
for num in nums:
    rem=target-num
    if ((rem in nums)==True and (nums.index(rem) != nums.index(num))):
        print(nums.index(num))
        print(nums.index(rem))
        break
 </sol>
</template>
<suffix>

</suffix>
<suffix_invisible>

</suffix_invisible>
```

# Public Test Cases

## Input 1

```
2,7,11,15
9

```

## Output 1

```
0
1
```


# Private Test Cases

## Input 1

```
3 2 4

```

## Output 1

```
1
2
```


