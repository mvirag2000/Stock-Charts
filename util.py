def print_stats(f):
	"""Too bad there is no overloading in Python"""
	import pandas as pd
	if isinstance(f, pd.DataFrame):
		frame_stats(f)
	else:
		series_stats(f)

def frame_stats(df):
	"""Prints summary information about DataFrame"""
	import numpy as np
	print('\n')
	print(df.columns)
	print('\nCOL\t MIN\t MAX\t MEAN')
	for i in df.columns:
		min = np.min(df[i])
		max = np.max(df[i])
		r = df[i]
		try:
			r = [float(a) for a in r]
			mean = np.mean(r)
		except (ValueError, TypeError):
			mean = 'NaN'
		print(str(i) + '\t' + str(min) + '\t' + str(max) + '\t' + str(mean))
	print('Rows = ' + str(df.shape[0]))
	print('Cols = ' + str(df.shape[1]))
	
def series_stats(s):
	"""Prints summary information about series"""
	import numpy as np
	print('\n')
	print('\nMIN\t MAX\t MEAN')
	print(str(min(s)) + '\t' + str(max(s)) + '\t' + str(np.mean(s)))
	print('Rows = ' + str(s.shape[0]))	
	print('Cols = ' + str(s.shape[1]))
	
def pairs(n):
	"""Number of times n people clink glasses when toasting"""
	return n * (n-1) / 2
