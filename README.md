e is shorthand notation for pandas

### Approach

- The class `DF` extends pandas.DataFrame
- Common operations are designated by single letters
- All operations are available as methods
- All operations are available as functions
- Methods modify the instance in-place
- Functions return a new instance

### Functionality

|Operation|Function|
|---------|--------|
|Select|s(data, selection)|
|Filter|f(data, condition)|
|Join|j(data, left, right, other, operation)|
|Append|a(data, other)|
|Extend|e(data, name, other)|
|Map|m(data, name, function)|
|Reduce|r(data, function, keep)|
|Pivot|p(data, keep, pivot, value)|
|Unpivot|u(data, keep, variable, values)|

### Example

```{python}
import e

data = e.DF({
	'x': [11, 2, 3, 66, 7, 2, 1, 5, 5],
	'y': [ 0, 4, 0,  4, 7, 8, 9, 5, 5],
	'z': [22, 2, 7, 25, 7, 0, 6, 6, 3]
	})

data.s(['x', 'y'])

data
```

### Reference

