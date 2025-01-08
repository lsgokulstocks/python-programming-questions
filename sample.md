---
title: Sample Title
tags: ['sample tag1', 'sample tag2']
---

# Problem Statement

# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>
def trial_question(a:int,b:int):

<sol> return a+b </sol>
</template>
<suffix>

</suffix>
<suffix_invisible>
{% include './function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1


```
dummy_equal(
    9, trial_question(5,4)
)
```

## Output 1

```
9
```


# Private Test Cases

## Input 1

```
dummy_equal(
    9, trial_question(5,4)
)
```

## Output 1

```
9
```
