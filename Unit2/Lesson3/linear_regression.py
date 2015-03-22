import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# import data into a pandas dataframe
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

# check the first few records in the dataset
loansData.head()

# remove the "%" from loansData['Interest.Rate'], loansData['Debt.To.Income.Ratio']
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x[:-1])
loansData['Debt.To.Income.Ratio'] = loansData['Debt.To.Income.Ratio'].map(lambda x: x[:-1])
# remove the " months" from loansData['Loan.Length']
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x[:-7])
# take the first number in FICO score range for loansData['FICO.Range']
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split("-")[0]))


"""
    LESSON 2 MATERIAL
"""
# plot the FICO Score as a histogram
plt.figure()
a = loansData['FICO.Score'].hist()
b = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()


"""
    LESSON 3 MATERIAL
"""
# set data to vars for easy ref
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# put columns together to make an input matrix
x = np.column_stack([x1,x2])

# create the linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# Print out the results to Std out
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
