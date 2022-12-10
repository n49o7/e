e is shorthand notation for pandas

### Approach

- The class `DF` extends pandas.DataFrame
- Common operations are designated by single letters
- Methods overwrite the instance in-place
- Indexes are not supported

### Functionality

**Select**
```{python}
s(*self*, selection)
selection (str or list): column name or list of column names
```

**Filter**
```{python}
f(*self*, condition)
condition (list): list of booleans
```
**Join**
```{python}
j(*self*, left, right, other, operation)
left (str): column name in the current DF
right (str): column name in the joined DF
other (DF): joined DF
operation (str): o, i, l, r or c
```

**Append**
```{python}
a(*self*, other)
other (DF): DF containing the rows to add
```

**Extend**
```{python}
e(*self*, name, other)
name (str): name of the new column
other (list): values in the new column
```

**Map**
```{python}
m(*self*, name, function)
name (str): name of the new column
function (function(row)): function returning the values based on other columns
```

**Reduce**
```{python}
r(*self*, function, keep)
function (function(row, next_row)): reducing function
keep (str or list): columns excluded from the reduce operation
```

**Pivot**
```{python}
p(*self*, keep, pivot, value)
keep (str or list): columns excluded from the pivot operation
pivot (str): name of the column to pivot
value (str): name of the column containing the values
```

**Unpivot**
```{python}
u(*self*, keep, variable, values)
keep (str or list): columns excluded from the melt operation
variable (str): name of the column containing the previous column names
values (values): name of the column contaning the values
```

### Example

```{python}
import e

data = e.DF({
	'x': [11, 2, 3, 66, 7, 2, 1, 5, 5],
	'y': [ 0, 4, 0,  4, 7, 8, 9, 5, 5],
	'z': [22, 2, 7, 25, 7, 0, 6, 6, 3]
	})

data.s(['x', 'y'])

print(data)
```

See `demo.py` for more examples.
