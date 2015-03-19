import collections
import pandas as pd
import matplotlib.pyplot as plt

# read csv file into pandas
data = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
data.dropna(inplace=True)

# count the number of instances of open credit lines
open_credit_freq = collections.Counter(data['Open.CREDIT.Lines'])

# plot the number of open credit lines as a hist, boxplot
plt.figure()
plt.bar(open_credit_freq.keys(), open_credit_freq.values(), width=1)
data.boxplot(column='Open.CREDIT.Lines')
plt.show()
