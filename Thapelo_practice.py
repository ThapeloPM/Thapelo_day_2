# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:44:05 2024

@author: Thapelo
"""

# This is my first comment
"""
I am lerning to code
"""

import pandas
file = pandas.read_csv("country_data.csv")

print(file)

"""
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
#   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes
None
"""

print(file.describe())

"""
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

file = pandas.read_csv("iris.csv")

print(file)
"""
[8 rows x 9 columns]
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
"""
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
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
"""

column_names = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

file = pandas.read_csv("housing_data.csv", names = column_names)

print(file)
"""
           A     B      C    D      E  ...      J     K       L     M     N
0    0.00632  18.0   2.31  0.0  0.538  ...  296.0  15.3  396.90  4.98  24.0
1    0.02731   0.0   7.07  0.0  0.469  ...  242.0  17.8  396.90  9.14  21.6
2    0.02729   0.0   7.07  0.0  0.469  ...  242.0  17.8  392.83  4.03  34.7
3    0.03237   0.0   2.18  0.0  0.458  ...  222.0  18.7  394.63  2.94  33.4
4    0.06905   0.0   2.18  0.0  0.458  ...  222.0  18.7  396.90  5.33  36.2
..       ...   ...    ...  ...    ...  ...    ...   ...     ...   ...   ...
501  0.06263   0.0  11.93  0.0  0.573  ...  273.0  21.0  391.99  9.67  22.4
502  0.04527   0.0  11.93  0.0  0.573  ...  273.0  21.0  396.90  9.08  20.6
503  0.06076   0.0  11.93  0.0  0.573  ...  273.0  21.0  396.90  5.64  23.9
504  0.10959   0.0  11.93  0.0  0.573  ...  273.0  21.0  393.45  6.48  22.0
505  0.04741   0.0  11.93  0.0  0.573  ...  273.0  21.0  396.90  7.88  11.9

[506 rows x 14 columns]
"""
print(file.info())
"""
#   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   A       506 non-null    float64
 1   B       506 non-null    float64
 2   C       506 non-null    float64
 3   D       506 non-null    float64
 4   E       506 non-null    float64
 5   F       506 non-null    float64
 6   G       506 non-null    float64
 7   H       506 non-null    float64
 8   I       506 non-null    int64  
 9   J       506 non-null    float64
 10  K       506 non-null    float64
 11  L       506 non-null    float64
 12  M       506 non-null    float64
 13  N       452 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.5 KB
None

# They are non-values in column N
"""

print(file.describe())
"""
                A           B           C  ...           L           M           N
count  506.000000  506.000000  506.000000  ...  506.000000  506.000000  452.000000
mean     1.269195   13.295257    9.205158  ...  332.791107   11.537806   23.750442
std      2.399207   23.048697    7.169630  ...  125.322456    6.064932    8.808602
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049443    0.000000    3.440000  ...  364.995000    6.877500   18.500000
50%      0.144655    0.000000    6.960000  ...  390.660000   10.380000   21.950000
75%      0.819623   18.100000   18.100000  ...  395.615000   15.015000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000

[8 rows x 14 columns]
"""
file = pandas.read_csv("insurance_data.csv",skiprows=(5))

print(file)
"""
[8 rows x 14 columns]
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

print(file.info())
"""
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   X       63 non-null     int64  
 1   Y       63 non-null     float64
dtypes: float64(1), int64(1)
memory usage: 1.1 KB
None
"""
print(file.describe())
"""
                X           Y
count   63.000000   63.000000
mean    22.904762   98.187302
std     23.351946   87.327553
min      0.000000    0.000000
25%      7.500000   38.850000
50%     14.000000   73.400000
75%     29.000000  140.000000
max    124.000000  422.200000
"""



# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

M = ("Male")
F = ("Female")

C1 = M
C2 = M
C3 = F
C4 = M

print(C1)
print(C2)

# Using Lists

age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
print(age[10])

age = [30,40,30,49,22,35,22,46,29,25,39]

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

# Storing Text
C2 = M
C3 = M
C4 = F

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:2]

      d = {'key1': 'value1', 'key2': 'value2'}

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'


