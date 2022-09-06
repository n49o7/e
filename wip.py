import numpy as np
import pandas as pd

a = ...

df = pd.DataFrame({
	'x': [11, 2, 3, 66, 7, 2, 1, 5, 5],
	'y': [ 0, 4, 0,  4, 7, 8, 9, 5, 5],
	'z': [22, 2, 7, 25, 7, 0, 6, 6, 3]
	})

import e

print(e._functions)

x = e.Data(df)

print(x)

o = {'i':[1, 2, 3], 'variable': [65, 93, 25]}

df = e.Data(pd.DataFrame(o))

print(x.e('yo', o['i']))