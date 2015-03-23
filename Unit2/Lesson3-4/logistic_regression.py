# import all the libraries that we'll need for these lessons
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm # http://statsmodels.sourceforge.net/stable/

# imports the code from the cleaned_data.py file found in this folder
import cleaned_data
loansData = cleaned_data.clean_up_data()

# create a column for >12% interest rate
loansData['TF.Interest'] = loansData['Interest.Rate'].map(lambda x: True if x > 12 else False)
# create a column for statsmodel intercept == 1.0
loansData['StatsModel.Intercept'] = loansData['Interest.Rate'].map(lambda x: 1.0)
# List of the column names of independent variables, including the intercept
ind_vars = ['Interest.Rate', 'FICO.Score', 'Loan.Amount', 'StatsModel.Intercept']

p_cutoff = 0.7 # prob less that 70% means we wouldn't get the loan

# define the logistic regression model
model = sm.Logit(df['TF.Interest'], df[ind_vars])
# fit the model for the results
results = logit.fit()
# get fitted coefficients from the results
coeff = result.params
print coeff

# def logistic_function (FICO, LoanAmount):
#     interest_rate = −60.125 + (0.087423*FicoScore) − (0.000174*LoanAmount)
#     p(x) = lambda x: 1/(1 + e^(intercept + (0.087423*FicoScore) − (0.000174*LoanAmount)))
