---
title: Simple-Select
date: 2024-11-22
author: Your Name
cell_count: 4
score: 0
---

```python
from pypika import Query, Table

# Define a table
users = Table("users")

# Build a SELECT query
query = Query.from_(users).select(users.id, users.name)



```


```python
!pip install pypika
```

    Requirement already satisfied: pypika in /opt/homebrew/Caskroom/miniconda/base/envs/py312/lib/python3.12/site-packages (0.48.9)



```python
print(query)  # Output: SELECT "id","name" FROM "users"
```

    SELECT "id","name" FROM "users"



```python

```


---
**Score: 0**