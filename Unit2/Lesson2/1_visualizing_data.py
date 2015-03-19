import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# read csv file into pandas
data = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
data.dropna(inplace=True)

# plot the Amount Requested data as a boxplot, hist
plt.figure()
data.boxplot(column='Amount.Requested')
data.hist(column='Amount.Requested')
plt.show()
# plot the same data as a qq plot
plt.figure()
stats.probplot(data['Amount.Requested'], dist="norm", plot=plt)
plt.show()
