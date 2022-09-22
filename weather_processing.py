"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import pandas as pd
import numpy as np


# TODO Import the dataset 

path = r'./data/weather_dataset.data'

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data = pd.read_csv(path, sep="\s+")
print(data)
data['datetime'] = pd.to_datetime(dict(year=data.Yr + 1900, month=data.Mo, day=data.Dy))

datetime_index = pd.DatetimeIndex(data['datetime'].values)
data.drop(['Yr', 'Mo', 'Dy'], axis=1, inplace=True)


# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

def cast_values(x):
    try:
        return float(x.replace(',', '.'))
    except:
        return None

data.iloc[:, :-1] = data.iloc[:, :-1].applymap(cast_values)
print(data.info())
  


# TODO Write a function in order to fix date (this relate only to the year info) and apply it

# but we replaced first 3 columns in the first step
# def fix_year(y):
#     return 1900 + y

# data['Yr'] = data['Yr'].apply(fix_year)


# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data.set_index(datetime_index, inplace=True)
data.drop(['datetime'], axis=1, inplace=True)

# TODO Compute how many values are missing for each location over the entire record
count_of_missing_values = data.isna().sum()
print(count_of_missing_values)

# TODO Compute how many non-missing values there are in total
print(f'There are {data.count().sum()} non-nan values')

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
print(f'Mean windspeeds over the entire dataset is {np.round(data.stack().mean(), 2)}')

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
data_stat = data.describe().loc[['min', 'max', 'mean', 'std'], :]
print(data_stat)

# TODO Find the average windspeed in January for each location
print('Mean of windspeed in January:')
jan_mean_windspeed = data.resample('M').mean()[::12].mean()
print(jan_mean_windspeed)

# TODO Downsample the record to a yearly frequency for each location
y_windspeed = data.resample('Y')

# TODO Downsample the record to a monthly frequency for each location
m_windspeed = data.resample('M')

# TODO Downsample the record to a weekly frequency for each location
w_windspeed = data.resample('W')

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
w_windspeed_2 = data[1:].resample('7D')
w_mean = w_windspeed_2.agg(['min', 'max', 'mean', 'std'])