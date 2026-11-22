```python
import pandas as pd
```


```python
pd.__version__
```




    '3.0.3'




```python
emp = pd.read_excel(r'C:\My-Drive\Learning\repositories\notes-repo\AI-Naresh-IT\raw_data.xlsx')
```


```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience#$</td>
      <td>34 years</td>
      <td>Mumbai</td>
      <td>5^00#0</td>
      <td>2+</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy^</td>
      <td>Testing</td>
      <td>45' yr</td>
      <td>Bangalore</td>
      <td>10%%000</td>
      <td>&lt;3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Uma#r</td>
      <td>Dataanalyst^^#</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1$5%000</td>
      <td>4&gt; yrs</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Ana^^lytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>2000^0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam*</td>
      <td>Statistics</td>
      <td>67-yr</td>
      <td>NaN</td>
      <td>30000-</td>
      <td>5+ year</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55yr</td>
      <td>Delhi</td>
      <td>6000^$0</td>
      <td>10+</td>
    </tr>
  </tbody>
</table>
</div>




```python
emp.isnull().sum()
```




    Name        0
    Domain      0
    Age         2
    Location    2
    Salary      0
    Exp         1
    dtype: int64




```python
emp.isna().sum()
```




    Name        0
    Domain      0
    Age         2
    Location    2
    Salary      0
    Exp         1
    dtype: int64




```python
emp.columns
```




    Index(['Name', 'Domain', 'Age', 'Location', 'Salary', 'Exp'], dtype='str')




```python
emp.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 6 columns):
     #   Column    Non-Null Count  Dtype
    ---  ------    --------------  -----
     0   Name      6 non-null      str  
     1   Domain    6 non-null      str  
     2   Age       4 non-null      str  
     3   Location  4 non-null      str  
     4   Salary    6 non-null      str  
     5   Exp       5 non-null      str  
    dtypes: str(6)
    memory usage: 619.0 bytes
    

# Data Cleaning or Data Cleansing


```python
emp['Name']
```




    0      Mike
    1    Teddy^
    2     Uma#r
    3      Jane
    4    Uttam*
    5       Kim
    Name: Name, dtype: str




```python
emp['Name'] = emp['Name'].str.replace(r'\W','',regex=True)
```


```python
emp['Name']
```




    0     Mike
    1    Teddy
    2     Umar
    3     Jane
    4    Uttam
    5      Kim
    Name: Name, dtype: str




```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience#$</td>
      <td>34 years</td>
      <td>Mumbai</td>
      <td>5^00#0</td>
      <td>2+</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45' yr</td>
      <td>Bangalore</td>
      <td>10%%000</td>
      <td>&lt;3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst^^#</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1$5%000</td>
      <td>4&gt; yrs</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Ana^^lytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>2000^0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67-yr</td>
      <td>NaN</td>
      <td>30000-</td>
      <td>5+ year</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55yr</td>
      <td>Delhi</td>
      <td>6000^$0</td>
      <td>10+</td>
    </tr>
  </tbody>
</table>
</div>




```python
emp['Domain'] = emp['Domain'].str.replace(r'\W','',regex=True)
```


```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34 years</td>
      <td>Mumbai</td>
      <td>5^00#0</td>
      <td>2+</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45' yr</td>
      <td>Bangalore</td>
      <td>10%%000</td>
      <td>&lt;3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1$5%000</td>
      <td>4&gt; yrs</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>2000^0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67-yr</td>
      <td>NaN</td>
      <td>30000-</td>
      <td>5+ year</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55yr</td>
      <td>Delhi</td>
      <td>6000^$0</td>
      <td>10+</td>
    </tr>
  </tbody>
</table>
</div>




```python
emp['Location'] = emp['Location'].str.replace(r'\W','',regex=True)
```


```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34 years</td>
      <td>Mumbai</td>
      <td>5^00#0</td>
      <td>2+</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45' yr</td>
      <td>Bangalore</td>
      <td>10%%000</td>
      <td>&lt;3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1$5%000</td>
      <td>4&gt; yrs</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>2000^0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67-yr</td>
      <td>NaN</td>
      <td>30000-</td>
      <td>5+ year</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55yr</td>
      <td>Delhi</td>
      <td>6000^$0</td>
      <td>10+</td>
    </tr>
  </tbody>
</table>
</div>




```python
emp['Salary'] = emp['Salary'].str.replace(r'\W','',regex=True)
```


```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34 years</td>
      <td>Mumbai</td>
      <td>5000</td>
      <td>2+</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45' yr</td>
      <td>Bangalore</td>
      <td>10000</td>
      <td>&lt;3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15000</td>
      <td>4&gt; yrs</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>20000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67-yr</td>
      <td>NaN</td>
      <td>30000</td>
      <td>5+ year</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55yr</td>
      <td>Delhi</td>
      <td>60000</td>
      <td>10+</td>
    </tr>
  </tbody>
</table>
</div>




```python
emp['Age'] = emp['Age'].str.extract('(\\d+)')
```


```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34</td>
      <td>Mumbai</td>
      <td>5000</td>
      <td>2+</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45</td>
      <td>Bangalore</td>
      <td>10000</td>
      <td>&lt;3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15000</td>
      <td>4&gt; yrs</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>20000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67</td>
      <td>NaN</td>
      <td>30000</td>
      <td>5+ year</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55</td>
      <td>Delhi</td>
      <td>60000</td>
      <td>10+</td>
    </tr>
  </tbody>
</table>
</div>




```python
emp['Exp'] = emp['Exp'].str.extract('(\\d+)')
```


```python
emp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34</td>
      <td>Mumbai</td>
      <td>5000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45</td>
      <td>Bangalore</td>
      <td>10000</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>20000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67</td>
      <td>NaN</td>
      <td>30000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55</td>
      <td>Delhi</td>
      <td>60000</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_data = emp.copy()
clean_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34</td>
      <td>Mumbai</td>
      <td>5000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45</td>
      <td>Bangalore</td>
      <td>10000</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>NaN</td>
      <td>Hyderbad</td>
      <td>20000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67</td>
      <td>NaN</td>
      <td>30000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55</td>
      <td>Delhi</td>
      <td>60000</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



# 1- Missing value treatment


```python
import numpy as np
```


```python
clean_data['Age'] = clean_data['Age'].fillna(np.mean(pd.to_numeric(clean_data['Age'])))
```


```python
clean_data['Age']
```




    0       34
    1       45
    2    50.25
    3    50.25
    4       67
    5       55
    Name: Age, dtype: object




```python
clean_data['Exp'] = clean_data['Exp'].fillna(np.mean(pd.to_numeric(clean_data['Exp'])))
clean_data['Exp']
```




    0      2
    1      3
    2      4
    3    4.8
    4      5
    5     10
    Name: Exp, dtype: object




```python
clean_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34</td>
      <td>Mumbai</td>
      <td>5000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45</td>
      <td>Bangalore</td>
      <td>10000</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>50.25</td>
      <td>NaN</td>
      <td>15000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>50.25</td>
      <td>Hyderbad</td>
      <td>20000</td>
      <td>4.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67</td>
      <td>NaN</td>
      <td>30000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55</td>
      <td>Delhi</td>
      <td>60000</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_data['Location']
```




    0       Mumbai
    1    Bangalore
    2          NaN
    3     Hyderbad
    4          NaN
    5        Delhi
    Name: Location, dtype: str




```python
clean_data['Location'] = clean_data['Location'].fillna(clean_data['Location'].mode()[0])
```


```python
clean_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Domain</th>
      <th>Age</th>
      <th>Location</th>
      <th>Salary</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Datascience</td>
      <td>34</td>
      <td>Mumbai</td>
      <td>5000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Teddy</td>
      <td>Testing</td>
      <td>45</td>
      <td>Bangalore</td>
      <td>10000</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Umar</td>
      <td>Dataanalyst</td>
      <td>50.25</td>
      <td>Bangalore</td>
      <td>15000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jane</td>
      <td>Analytics</td>
      <td>50.25</td>
      <td>Hyderbad</td>
      <td>20000</td>
      <td>4.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uttam</td>
      <td>Statistics</td>
      <td>67</td>
      <td>Bangalore</td>
      <td>30000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kim</td>
      <td>NLP</td>
      <td>55</td>
      <td>Delhi</td>
      <td>60000</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
