# import all the libraries that we'll need for these lessons
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm # http://statsmodels.sourceforge.net/stable/

def clean_up_data():
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
    # make sure values are in float or int format instead of strings
    loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x))
    loansData['Amount.Requested'] = loansData['Amount.Requested'].map(lambda x: int(x))
    return loansData
