# TODO: avoid depending on DataFrames

import pandas as pd
import types

def s(data, selection):
	# Select
	return data[selection]

def f(data, condition):
	# Filter
	return data[condition]

def j(data, left, right, other, operation):
	# Join
	o = {
		'o': 'outer',
		'i': 'inner',
		'l': 'left',
		'r': 'right',
		'c': 'cross'
		}
	return pd.merge(
		left=data,
		right=other,
		left_on=left,
		right_on=right,
		how=o[operation]
		)

def a(data, other):
	# Append
	return pd.concat(
		data,
		other,
		ignore_index=True
		)

def e(data, name, other):
	# Extend
	# BUG: name == name
	return data.assign(name=other)

def m(data, name, function):
	# Map
	data[name] = data.apply(function, axis='columns')
	return data

def r(data, function, keep):
	# Reduce
	return data.groupby(keep).agg(function).reset_index()

def p(data, keep, pivot, value):
	# Pivot
	return data.pivot(
		index=keep,
		columns=pivot,
		values=value
		)

def u(data, keep, variable, values):
	# Unpivot
	return data.melt(
		id_vars=keep,
		var_name=variable,
		value_name=values
		)

def is_function(_f):
	return isinstance(_f, types.FunctionType)

_functions = [(_n, _t) for (_n, _t) in locals().items() if is_function(_t)]

class Data(pd.DataFrame):
	pass

for _n, _f in _functions:
    setattr(Data, _n, _f)

def read(filepath, **kwargs):
	return pd.read_csv(filepath, **kwargs)