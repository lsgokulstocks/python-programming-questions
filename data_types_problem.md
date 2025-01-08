---
title: Add 2 numbers which have been type casted to string
tags: ['list','list manipulation','slicing']
---

# Problem Statement

String Addition

**Example**
```
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# Namaste
</prefix>
<template>
def add_string_numbers(num1:str, num2:str)-> str:
    '''
    Given 2 numbers in as type str, return their sum as a str
    Quite ez ik....
    '''
    <los>...</los>
    <sol>return str(int(num1)+int(num2))</sol>
</template>
<suffix>
# some suffix
</suffix>
<suffix_invisible>
{% include './function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
dummy_check(
    add_string_numbers('42', '8'),
    '50'
)
```

## Output 1

```
'50'
```

## Input 2

```
dummy_check(
    add_string_numbers('50', '-5'),
    '45'
)
```

## Output 2

```
'45'
```

## Input 3 

```
dummy_check(
    add_string_numbers('69', '0'),
    '69'
)
```

## Output 3

```
'69'
```

# Private Test Cases

## Input 1

```
n = '102'
m='201'
dummy_check(
    add_string_numbers(n, m),
    '303'
)
dummy_check(
    add_string_numbers(n, n),
    '204'
)
dummy_check(
    add_string_numbers(m,m),
    '402'
)
```

## Output 1

```
'303'
'204'
'402'
```