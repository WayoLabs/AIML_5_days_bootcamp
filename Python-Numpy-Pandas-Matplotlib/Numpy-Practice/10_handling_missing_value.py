import numpy as np 

data = np.array([[1, 2, np.nan],
                 [4, np.nan, 6],
                 [7, 8, 9]])

# Fill NaNs with column means
col_mean = np.nanmean(data, axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(col_mean, inds[1])

print(data)
