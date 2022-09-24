import pandas as pd
import types

# Utilities

def read(filepath, **kwargs):
	return pd.read_csv(filepath, **kwargs)

# Class

class DF(pd.DataFrame):

	def s(self, selection):
		# Select
		self = DF(self[selection])
		return self

	def f(self, condition):
		# Filter
		# TODO: do not rely on the object
		self = DF(self[condition])
		return self

	def j(self, left, right, other, operation):
		# Join
		o = {
			'o': 'outer',
			'i': 'inner',
			'l': 'left',
			'r': 'right',
			'c': 'cross'
			}
		self = DF(pd.merge(
			left=self,
			right=other,
			left_on=left,
			right_on=right,
			how=o[operation]
			))
		return self

	def a(self, other):
		# Append
		self = DF(pd.concat(
			self,
			other,
			ignore_index=True
			))
		return self

	def e(self, name, other):
		# Extend
		self[name] = other
		return self

	def m(self, name, function):
		# Map
		self[name] = self.apply(function, axis='columns')
		return self

	def r(self, function, by, selection):
		# Reduce
		self = DF(self.groupby(keep)[selection].agg(function).reset_index())
		return self

	def p(self, keep, pivot, value):
		# Pivot
		self = DF(self.pivot(
			index=keep,
			columns=pivot,
			values=value
			))
		return self

	def u(self, keep, variable, values):
		# Unpivot
		self = DF(self.melt(
			id_vars=keep,
			var_name=variable,
			value_name=values
			))
		return self