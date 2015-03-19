# For this lesson I will be diverging from the Thinkful material and using
# the Kaggle Titanic dataset instead (train.csv). This is a far dirtier and,
# in many ways, more realistic exmaple of the datasets in you might encounter.
# I highly encourage you all to dl and work along with these examples as well as
# working the lesson exercises.
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

# read csv file into pandas
data = pd.read_csv('train.csv')

# keep only rows where Fare in a finite number
r = data[np.isfinite(data['Fare'])]
# remove outliers above 100 and less than or equal to 0
r = r['Fare'][(r['Fare'] <= 100) & (r['Fare'] > 0)]

# plot figure in a hist and QQ plot
plt.figure()
data.boxplot(column="Fare")
plt.subplots()
stats.probplot(r, dist='norm', plot=plt)
plt.subplots()
r.hist()
plt.show()
