e is shorthand notation for pandas

### Approach

- The class `DF` extends pandas.DataFrame
- Common operations are designated by single letters
- Methods overwrite the instance in-place

### Functionality

|Operation|Method|
|---------|--------|
|Select|s(*self*, selection)|
|Filter|f(*self*, condition)|
|Join|j(*self*, left, right, other, operation)|
|Append|a(*self*, other)|
|Extend|e(*self*, name, other)|
|Map|m(*self*, name, function)|
|Reduce|r(*self*, function, keep)|
|Pivot|p(*self*, keep, pivot, value)|
|Unpivot|u(*self*, keep, variable, values)|

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

### Reference

