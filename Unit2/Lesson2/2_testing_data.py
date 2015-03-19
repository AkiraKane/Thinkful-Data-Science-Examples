import collections
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# read csv file into pandas
data = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
data.dropna(inplace=True)

# count the number of instances of open credit lines
open_credit_freq = collections.Counter(data['Open.CREDIT.Lines']

# plot the number of open credit lines as a hist
plt.figure()
plt.bar(open_credit_freq.keys(), open_credit_freq.values(), width=1)
plt.show()

# Run a Chi-Squared Test on the data
# Step 1: only include categories with freqs greater than or equal to 5
chi_redux = {}
for k in open_credit_freq:
    if open_credit_freq[k] >= 5:
        chi_redux[k] = open_credit_freq[k]
# Step 2: Calculate chi and p-value
chi, p = stats.chisquare(chi_redux.values())
print chi
print p
