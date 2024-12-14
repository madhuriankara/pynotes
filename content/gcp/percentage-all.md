---
title: Percentage-All
date: 2024-12-13
author: Your Name
cell_count: 5
score: 5
---

```python
#What percentage of land is arable, used for crops, or categorized as other for each country?
```


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
def get_percentage():
    query = """
    SELECT country, 
       arable_ AS arable_percentage, 
       crops_ AS crops_percentage, 
       other_ AS other_percentage
FROM `plucky-order-444214-g8.student_data.country_table`;
    """
    result = client.query(query)
    print("The percentages of all is:")
    for i in result:
        print(f'{i.arable_percentage} -  {i.crops_percentage} - {i.other_percentage}')

get_percentage()
```

    The percentages of all is:
    553 -  1079 - 3391
    733 -  11 - 9256
    2168 -  64 - 7768
    4522 -  91 - 5387
    2609 -  227 - 7165
    3335 -  32 - 6345
    86 -  149 - 8991
    1662 -  1398 - 694
    103 -  19 - 9878
    1961 -  217 - 7822
    496 -  2 - 9502
    1304 -  0 - 8696
    241 -  24 - 9735
    129 -  0 - 871
    452 -  108 - 944
    214 -  0 - 9786
    0 -  0 - 100
    2779 -  953 - 6268
    2328 -  4 - 7632
    2813 -  313 - 6874
    0 -  0 - 100
    1667 -  0 - 8333
    1963 -  271 - 7766
    372 -  14 - 9614
    1083 -  83 - 8834
    1213 -  22 - 8765
    872 -  139 - 8989
    77 -  0 - 9923
    2787 -  87 - 7126
    282 -  563 - 9155
    1315 -  78 - 8607
    267 -  183 - 955
    73 -  11 - 9916
    0 -  14 - 9974
    164 -  27 - 9809
    167 -  9 - 9824
    2522 -  443 - 7035
    6 -  225 - 9715
    278 -  24 - 9698
    322 -  25 - 9653
    287 -  48 - 9665
    2 -  0 - 9998
    0 -  0 - 100
    655 -  4 - 9341
    65 -  1 - 9934
    4 -  0 - 9996
    48 -  1 - 9951
    99 -  0 - 9901
    354 -  1 - 9645
    167 -  4 - 9829
    1208 -  79 - 8713
    661 -  92 - 9247
    0 -  0 - 100
    1818 -  455 - 7727
    1053 -  0 - 8947
    8 -  4 - 988
    3721 -  233 - 6046
    285 -  171 - 9544
    696 -  9 - 9215
    20 -  667 - 7333
    385 -  0 - 9615
    242 -  167 - 9591
    441 -  588 - 8971
    3305 -  76 - 5935
    667 -  20 - 7333
    2265 -  1033 - 6702
    585 -  493 - 8922
    3185 -  1207 - 5608
    14 -  5 - 9981
    588 -  2941 - 6471
    1124 -  355 - 8521
    1254 -  503 - 8243
    244 -  15 - 9741
    283 -  1161 - 6009
    955 -  322 - 8723
    1607 -  1016 - 7377
    1038 -  943 - 8019
    20 -  0 - 80
    10 -  0 - 90
    1594 -  194 - 8212
    736 -  198 - 9066
    76 -  23 - 9217
    395 -  552 - 9053
    1944 -  278 - 7778
    656 -  2295 - 7049
    1795 -  1795 - 641
    37 -  6 - 9957
    1462 -  916 - 7622
    233 -  0 - 9767
    295 -  92 - 9613
    1176 -  294 - 853
    6211 -  307 - 3482
    309 -  43 - 9648
    57 -  76 - 9867
    1519 -  97 - 8384
    2096 -  61 - 7843
    471 -  67 - 9462
    505 -  101 - 9394
    1132 -  723 - 8145
    38 -  35 - 9585
    0 -  0 - 100
    548 -  1761 - 7691
    1333 -  1667 - 70
    1895 -  1677 - 6428
    164 -  0 - 9836
    1386 -  157 - 7044
    24 -  1 - 75
    2936 -  646 - 6418
    1997 -  595 - 7408
    20 -  0 - 80
    10 -  15 - 75
    1739 -  1304 - 6957
    1095 -  465 - 844
    82 -  546 - 9372
    909 -  1636 - 7455
    274 -  5068 - 4658
    1667 -  3889 - 4444
    571 -  4571 - 4858
    0 -  0 - 100
    38 -  33 - 9929
    1304 -  435 - 8261
    87 -  435 - 8695
    46 -  144 - 981
    212 -  2438 - 5442
    64 -  2 - 9736
    2361 -  4306 - 3333
    0 -  0 - 100
    246 -  738 - 9016
    5 -  25 - 70
    1808 -  24 - 7952
    1443 -  19 - 8538
    3505 -  1402 - 5093
    31 -  14 - 9676
    286 -  2 - 9712
    3587 -  2332 - 4081
    296 -  52 - 9652
    51 -  13 - 9936
    975 -  1384 - 7641
    463 -  357 - 918
    1071 -  75 - 8854
    126 -  66 - 9808
    25 -  5 - 745
    1626 -  967 - 7407
    363 -  258 - 9379
    1067 -  882 - 8051
    395 -  228 - 9377
    507 -  103 - 9391
    2338 -  149 - 7513
    382 -  3 - 9615
    4926 -  296 - 4778
    None -  None - None
    51 -  3 - 946
    136 -  12 - 852
    625 -  4896 - 4479
    1278 -  21 - 8701
    222 -  1333 - 8445
    698 -  89 - 9213
    683 -  18 - 9299
    4615 -  221 - 5164
    2588 -  1065 - 6347
    708 -  3 - 929
    832 -  34 - 9134
    1144 -  386 - 847
    5621 -  161 - 4218
    1231 -  48 - 8721
    265 -  42 - 9693
    743 -  23 - 9234
    1219 -  96 - 8685
    2076 -  249 - 7675
    1718 -  195 - 8087
    1604 -  45 - 8351
    2967 -  47 - 6986
    2109 -  442 - 7449
    4002 -  192 - 5806
    398 -  305 - 5715
    5009 -  206 - 4785
    2226 -  181 - 7593
    4591 -  112 - 5297
    4082 -  225 - 5693
    3016 -  262 - 6722
    779 -  444 - 8777
    2895 -  2105 - 50
    1639 -  417 - 7944
    3093 -  331 - 6576
    169 -  1897 - 6413
    1786 -  1374 - 684
    1913 -  22 - 8065
    56 -  699 - 8741
    968 -  5 - 8982
    1087 -  13 - 89
    4054 -  1216 - 473
    222 -  0 - 9778
    1691 -  86 - 8223
    2328 -  4 - 7632
    5402 -  19 - 4579
    719 -  3 - 9278
    3385 -  59 - 6556
    211 -  878 - 7012
    None -  None - None
    7 -  0 - 9993
    152 -  3 - 8477
    9 -  0 - 91
    0 -  0 - 100
    2671 -  97 - 7232
    287 -  0 - 9713
    2175 -  781 - 7044
    2607 -  987 - 6406
    654 -  1 - 9345
    1042 -  61 - 8897
    2346 -  21 - 7633
    1755 -  23 - 8015
    2955 -  6 - 6985
    798 -  5 - 9197
    136 -  296 - 8344
    3353 -  207 - 644
    25 -  0 - 75
    267 -  19 - 9714
    1299 -  131 - 857
    289 -  4 - 9671
    154 -  125 - 8335
    1281 -  258 - 8461
    495 -  3 - 9502
    808 -  98 - 9094
    3129 -  296 - 6575
    73 -  35 - 9235
    544 -  274 - 4286
    1035 -  7 - 8895



```python

```


---
**Score: 5**