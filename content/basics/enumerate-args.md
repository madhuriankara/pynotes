---
title: Enumerate-Args
date: 2025-01-22
author: Your Name
cell_count: 3
score: 0
---

```python
def print_everything(*args):
        for count, thing in enumerate(args):
            print( '{0}. {1}'.format(count, thing))
```


```python
print_everything('apple', 'banana', 'cabbage', 'spinach')
```

    0. apple
    1. banana
    2. cabbage
    3. spinach



```python

```


---
**Score: 0**
