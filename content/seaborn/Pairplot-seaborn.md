---
title: Pairplot-Seaborn
date: 2024-12-03
author: Your Name
cell_count: 10
score: 10
---

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
days_list = [
    1, 1, 1, 1, 1,
    2, 2, 2, 2, 2,
    3, 3, 3, 3, 3
]
```


```python
learners_list = [
    'Madhuri','Sarvana','Soundarya','Steve','Hari',
    'Madhuri','Sarvana','Soundarya','Steve','Hari',
    'Madhuri','Sarvana','Soundarya','Steve','Hari'
]
```


```python
score_list = [
    0, 0, 0, 0, 0,
    535,300,510,580,205,
    880,490,600,625,205
]
```


```python
data = {
    'days':  days_list,
    'learners': learners_list,
    'score' : score_list
}
```


```python
df = pd.DataFrame(data)
```


```python
df_wide = df.pivot(index ='days', columns = 'learners', values = 'score')
```


```python
df_wide = pd.DataFrame(data)
```


```python
sns.pairplot(data= df_wide, hue="learners", vars=["score", "days"])
plt.title("Leaderboard")
plt.xlabel("Learners")
plt.ylabel("Score")
```




    Text(0, 0.5, 'Score')




    
![png](Pairplot-seaborn_files/Pairplot-seaborn_8_1.png)
    



```python

```


---
**Score: 10**