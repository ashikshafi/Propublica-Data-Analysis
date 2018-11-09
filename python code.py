import pandas as pd
import numpy as np

import glob
import re

dirlist=glob.glob("/Users/ashikshafi/Desktop/testing/Dataincubator/house-office-expenditures-with-readme/*[detail].*")

dfAll=[]
for i in dirlist:
    dfAll.append(pd.read_csv(i))


Data=pd.concat(dfAll, ignore_index=True)


Data.columns
Data.shape
Data.head(5)
Data.dtypes

# Preprocessing and finding sum of AMOUNT

Data.AMOUNT = Data.AMOUNT.apply(lambda x: str(x))

Data.AMOUNT = Data.AMOUNT.apply(lambda x: x.replace(',',''))

Data.AMOUNT = Data.AMOUNT.apply(lambda x: float(x))



Data.AMOUNT.isna().sum()
Data.AMOUNT.str.isnumeric().sum()

Data.AMOUNT.describe()

#The total expenditure (AMOUNT) is:

Data.AMOUNT.sum()


# Define the 'COVERAGE PERIOD' for each payment as the difference (in days) between 'END DATE' and 'START DATE'. What is the standard deviation in 'COVERAGE PERIOD'? Only consider payments with strictly positive amounts.

Data[Data["AMOUNT"]<0] = np.NaN

from datetime import datetime
import datetime as dt

#Converting to String values to avoid mismatch

Data["END DATE"].astype("category")

Data["START DATE"].astype("category")

#Deleting NaNs

Data[Data["END DATE"]=="nan"] = np.NaN

Data[Data["START DATE"]=="nan"] = np.NaN

#Checking patterns as date

Data["END DATE"].str.match(r'([A-Za-z])').sum()

#Checking the appearance

Data["END DATE"].tail(5)

Data["START DATE"].head(5)

#Converting to Datetime object. I had let python to figure out the time format.

EndDate=pd.to_datetime(Data["END DATE"])


StartDate=pd.to_datetime(Data["START DATE"])

#Creating COVERAGE PERIOD variable


timediff=EndDate-StartDate

timediff[1:5]
timediffint=timediff.values.astype(np.int64)
np.std(timediff.dt.days)


#What was the average annual expenditure with a 'START DATE' date between January 1, 2010 and December 31, 2016 (inclusive)?
#Only consider payments with strictly positive amounts.

Newdf=Data[(Data['START DATE']>='2010-01-01') & (Data['END DATE']<='2016-12-31')]

#Creating year as a variable by stripping of years from time delta object

Year = [d.strftime('%Y') if not pd.isnull(d) else '' for d in StartDate]

MeanAmount= Data["AMOUNT"].groupby(Year).sum()


np.mean(MeanAmount)

#Find the 'OFFICE' with the highest total expenditures with a 'START DATE' in 2016.
# For this office, find the 'PURPOSE' that accounts for the highest total expenditures.
# What fraction of the total expenditures (all records, all offices) with a 'START DATE' in 2016 do these expenditures amount to?

#Selecting the data starting in 2016

Data2016=Data[(Data['START DATE']>='2016-01-01')]


#Finding that greedy office

Data2016["AMOUNT"].groupby(Data2016["OFFICE"]).sum().sort_values()

# Turns out it is “GOVERNMENT CONTRIBUTIONS”

#Selecting data where Govt. Contribution was a payee

GovtContb=Data[Data['OFFICE']=="GOVERNMENT CONTRIBUTIONS"]

GovtContb["AMOUNT"].groupby(GovtContb['PURPOSE']).sum().sort_values()

#The highest expense is amount to
# Calculate fraction

6.200710e+08/sum(GovtContb.AMOUNT)

GovtContb.AMOUNT


#What was the highest average staff salary among all representatives in 2016? Assume staff sizes is equal to the number of unique payees in the 'PERSONNEL COMPENSATION' category for each representative.

#Reps who made a personal compensation

StaffData=Data[Data["CATEGORY"]=="PERSONNEL COMPENSATION"]

StaffData.shape

# Total number of staffs for All reps

StaffNum= len(list((StaffData["PAYEE"].groupby(StaffData["BIOGUIDE_ID"]).unique())))

len(StaffNum)

# Total staff salary by reps

StaffPayTotal=StaffData["AMOUNT"].groupby(StaffData["BIOGUIDE_ID"]).sum().sort_values()

#Average staff salary sorted

AvgStaffSalary=sorted(StaffPayTotal/StaffNum)




#What was the median rate of annual turnover in staff between 2011 and 2016 (inclusive)? Turnover for 2011 should be calculated as the fraction of a representative's staff from 2010 who did not carry over to 2011. Only consider representatives who served for at least 4 years and had staff size of at least 5 every year that they served.

#Select dataset from 2010-16 is Newdf

#Finding staff by year and by reps

[d.strftime('%Y') if not pd.isnull(d) else '' for d in StartDate.loc[2011-1-1:2016-12-31]]


Year2011-16 =list([d.strftime('%Y') if not pd.isnull(d) else '' for d in StartDate[2011-1-1:2016-12-31]]
)

StaffbyRep_n_Year=list(Newdf[“PAYEE"].groupby(Newdf[“BIOGUIDE_ID”], Year2011-16))
StaffbyYear=list(Newdf[“PAYEE"].groupby(Year2011-16))

#Sorting StaffbyRep_n_Year by Year2011-16
StaffbyYear=sorted(StaffbyRep_n_Year, key=Year2011-16)

#Finding Turnover:

Turnover=[StaffbyYear[i]/StaffbyYear[i-1] if StaffbyYear[i]< StaffbyYear[i-1] for i in StaffbyYear]

np.median(Turnover)

#What percentage of the expenditures of the top 20 spenders in 2016 come from members of the Democratic Party? Representatives are identified by their 'BIOGUIDE_ID', which can be used to look up representatives with ProPublica's Congress API(https://projects.propublica.org/api-docs/congress-api/members/#get-a-specic- member) to find their party affiliation. Consider an expenditure as being in 2016 if its 'START DATE' is in 2016.


["Even" if i%2==0 else "Odd" for i in range(10)]

[x for x in l if x < 5]

Turnover
for x, y in ll
	if StaffbyYear[i]< StaffbyYear[i-1]:
	Turnover=StaffbyYear[i]/StaffbyYear[i-1]
	else:
	Turnover= Turnover+0
Turnover=[]
	turnover= StaffbyRep_n_Year[i+1]-Sta StaffbyRep_n_Year ffbyyear[i]
	[x for x in turnover if x in StaffbyRep_n_Year < 5]

turnover=[i
for i in Staffbyyear:
    turnover=Staffbyyear[i+1]-Staffbyyear[i]


