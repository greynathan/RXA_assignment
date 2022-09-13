import pandas as pd

# opening the original csv and converting to dataframes
# One data frame for the map and one for machine learning
df = pd.read_csv('median_income_by_zip_code.csv')
df2 = pd.read_csv('median_income_by_zip_code.csv')
# opening a csv of zipcode coordinates and converting to dataframe
zip_coor = pd.read_csv('https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data')

# Looping through the dataframes of the MHI data
# for values with less than or equal to 0 Income I turn the map dataframe corresponding
# value to none and get rid of the machine learning data frame row all together
for ind in df.index:
    complete_row = True
    if df['2011_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2011_MHI'][ind] = None
        complete_row = False
    if df['2012_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2012_MHI'][ind] = None
        complete_row = False
    if df['2013_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2013_MHI'][ind] = None
        complete_row = False
    if df['2014_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2014_MHI'][ind] = None
        complete_row = False
    if df['2015_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2015_MHI'][ind] = None
        complete_row = False
    if df['2016_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2016_MHI'][ind] = None
        complete_row = False
    if df['2017_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2017_MHI'][ind] = None
        complete_row = False
    if df['2018_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2018_MHI'][ind] = None
        complete_row = False
    if df['2019_MHI'][ind] <= 0 or df['2011_MHI'][ind] == None:
        df['2019_MHI'][ind] = None
        complete_row = False
    if complete_row == False:
        df2.drop(labels = ind, axis = 0, inplace = True)
# After the loop is complete I have a data frame for machine learning with no missing 
# or inconclusive data and then I have a data frame including msising data for 
# visualization 

# for the dataframe for visualization I merge with the Zip code coordinates so that
# the data can be plotted on a map
df_map = df.join(zip_coor.set_index('ZIP'), on = 'zip_code').dropna()

# I save the dataframe for visualization and the dataframe for machine learning
df_map.to_parquet('df_map.parquet.gzip')
df2.to_parquet('df_ml.parquet.gzip')
print('done')






   