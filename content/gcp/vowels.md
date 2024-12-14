---
title: Vowels
date: 2024-12-13
author: Your Name
cell_count: 6
score: 5
---

```python
from google.cloud import bigquery
```


```python
client = bigquery.Client()
```

    /opt/homebrew/Caskroom/miniconda/base/envs/py312/lib/python3.12/site-packages/google/auth/_default.py:76: UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK without a quota project. You might receive a "quota exceeded" or "API not enabled" error. See the following page for troubleshooting: https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds. 
      warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)
    /opt/homebrew/Caskroom/miniconda/base/envs/py312/lib/python3.12/site-packages/google/auth/_default.py:76: UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK without a quota project. You might receive a "quota exceeded" or "API not enabled" error. See the following page for troubleshooting: https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds. 
      warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)



```python
def query_bigquery():
    query = """
        SELECT student_name FROM `plucky-order-444214-g8.student_data.student_data_madhuri`
        WHERE 
            (
                LENGTH(REGEXP_REPLACE(student_name, '[^aeiouAEIOU]', '')) = 3
            )
    """
    result = client.query(query)

    print("Students with exactly three vowels in their names:")
    for row in result:
        print(row.student_name)

query_bigquery()
```

    Students with exactly three vowels in their names:
    Amy Thomas
    Mary Carter
    Ann Griffin
    Karen Kelly
    Nancy Sanchez
    Mary Price
    Megan Ward
    Jane Smith
    Frank Morgan
    Frank Palmer
    John Doe
    Richard Ross
    Brandon Perry
    Raymond Murphy
    Justin Long
    Mark Roberts
    Bob Johnson
    Scott Howard
    Dennis Myers
    Chris Martin



```python

```


```python





```


```python

```


---
**Score: 5**