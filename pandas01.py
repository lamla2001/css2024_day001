# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:54:09 2024

@author: velle
"""

import pandas 
file = pandas.read_csv("country_data.csv")

print(file)

"""
runfile('C:/Users/velle/.spyder-py3/css2024/pandas01.py', wdir='C:/Users/velle/.spyder-py3/css2024')
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan

"""
print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
None

"""
print(file.describe())
"""
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
None
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000

"""
file =pandas.read_csv("iris.csv")

print(file)

"""
     sepal_length  sepal_width  petal_length  petal_width         species
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica

[150 rows x 5 columns]

"""
print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None

"""
print(file.describe())

file = pandas.read_csv("diab_data.csv")
print(file)

"""
    preg_count  glucose  bp  skinfold  insulin   BMI  predigree  age  class
0             6      148  72        35        0  33.6      0.627   50      1
1             1       85  66        29        0  26.6      0.351   31      0
2             8      183  64         0        0  23.3      0.672   32      1
3             1       89  66        23       94  28.1      0.167   21      0
4             0      137  40        35      168  43.1      2.288   33      1
..          ...      ...  ..       ...      ...   ...        ...  ...    ...
763          10      101  76        48      180  32.9      0.171   63      0
764           2      122  70        27        0  36.8      0.340   27      0
765           5      121  72        23      112  26.2      0.245   30      0
766           1      126  60         0        0  30.1      0.349   47      1
767           1       93  70        31        0  30.4      0.315   23      0

[768 rows x 9 columns]

"""
print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   preg_count  768 non-null    int64  
 1   glucose     768 non-null    int64  
 2   bp          768 non-null    int64  
 3   skinfold    768 non-null    int64  
 4   insulin     768 non-null    int64  
 5   BMI         768 non-null    float64
 6   predigree   768 non-null    float64
 7   age         768 non-null    int64  
 8   class       768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
None

"""
print(file.describe())

"""
       preg_count     glucose          bp  ...   predigree         age       class
count  768.000000  768.000000  768.000000  ...  768.000000  768.000000  768.000000
mean     3.845052  120.894531   69.105469  ...    0.471876   33.240885    0.348958
std      3.369578   31.972618   19.355807  ...    0.331329   11.760232    0.476951
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243750   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.250000   80.000000  ...    0.626250   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

[8 rows x 9 columns]
"""

file = pandas.read_csv("housing_data.csv")
print(file)

"""
0.00632   18   2.31    0  0.538  6.575  ...  1    296  15.3   396.9  4.98    24
0    0.02731  0.0   7.07  0.0  0.469  6.421  ...  2  242.0  17.8  396.90  9.14  21.6
1    0.02729  0.0   7.07  0.0  0.469  7.185  ...  2  242.0  17.8  392.83  4.03  34.7
2    0.03237  0.0   2.18  0.0  0.458  6.998  ...  3  222.0  18.7  394.63  2.94  33.4
3    0.06905  0.0   2.18  0.0  0.458  7.147  ...  3  222.0  18.7  396.90  5.33  36.2
4    0.02985  0.0   2.18  0.0  0.458  6.430  ...  3  222.0  18.7  394.12  5.21  28.7
..       ...  ...    ...  ...    ...    ...  ... ..    ...   ...     ...   ...   ...
500  0.06263  0.0  11.93  0.0  0.573  6.593  ...  1  273.0  21.0  391.99  9.67  22.4
501  0.04527  0.0  11.93  0.0  0.573  6.120  ...  1  273.0  21.0  396.90  9.08  20.6
502  0.06076  0.0  11.93  0.0  0.573  6.976  ...  1  273.0  21.0  396.90  5.64  23.9
503  0.10959  0.0  11.93  0.0  0.573  6.794  ...  1  273.0  21.0  393.45  6.48  22.0
504  0.04741  0.0  11.93  0.0  0.573  6.030  ...  1  273.0  21.0  396.90  7.88  11.9

[505 rows x 14 columns]

"""
print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 505 entries, 0 to 504
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   0.00632  505 non-null    float64
 1   18       505 non-null    float64
 2   2.31     505 non-null    float64
 3   0        505 non-null    float64
 4   0.538    505 non-null    float64
 5   6.575    505 non-null    float64
 6   65.2     505 non-null    float64
 7   4.09     505 non-null    float64
 8   1        505 non-null    int64  
 9   296      505 non-null    float64
 10  15.3     505 non-null    float64
 11  396.9    505 non-null    float64
 12  4.98     505 non-null    float64
 13  24       451 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.4 KB
None
"""
print(file.describe())
"""
          0.00632          18        2.31  ...       396.9        4.98          24
count  505.000000  505.000000  505.000000  ...  505.000000  505.000000  451.000000
mean     1.271696   13.285941    9.218812  ...  332.664158   11.550792   23.749889
std      2.400926   23.070598    7.170151  ...  125.414151    6.063900    8.818376
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049810    0.000000    3.440000  ...  364.610000    6.900000   18.500000
50%      0.144760    0.000000    6.960000  ...  390.640000   10.400000   21.900000
75%      0.825260   18.100000   18.100000  ...  395.600000   15.020000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000

[8 rows x 14 columns]
"""
file = pandas.read_csv("insurance_data.csv", skiprows=5)
print(file)
"""
     X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5

[63 rows x 2 columns]
"""
# Storing Data in Python 
#The data in python can be stored in using variables, lists, dictionaries and data frames.
 