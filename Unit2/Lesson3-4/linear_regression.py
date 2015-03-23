import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm # http://statsmodels.sourceforge.net/stable/

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
# set a column of data to a var for easy ref (out: pandas.core.series.Series)
intrate = loansData['Interest.Rate'].map(lambda x: float(x))
loanamt = loansData['Amount.Requested'].map(lambda x: int(x))
fico = loansData['FICO.Score']

# Create a numpy matrix from each of the Series, and then transpose that matrix
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# put independent vars matrices together to make an input matrix
x = np.column_stack([x1,x2])

# Create the linear regression model using statsmodels library.
# Fitting a model in statsmodels typically involves 3 easy steps:
#   1) Use the model class to describe the model
#   2) Fit the model using a class method
#   3) Inspect the results using a summary method
X = sm.add_constant(x)
model = sm.OLS(y,X) # Describe model
results = model.fit() # Fit model
print results.summary() # Summarize model
