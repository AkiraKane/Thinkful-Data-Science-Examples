import collections
import pandas as pd
import matplotlib.pyplot as plt

# read csv file into pandas
data = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
data.dropna(inplace=True)

# plot the number of open credit lines as a hist
plt.figure()
data.boxplot(column='Amount.Requested')
data.hist(column='Amount.Requested')
plt.show()
