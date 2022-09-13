from ML import prediction
import pandas as pd

# to begin I open the machine learning ready dataset and drop any missed NaN values
df = pd.read_parquet('df_ml.parquet.gzip')
df = df.dropna()

# Instantiate two helper arrays
zips = []
out = []

# Loop through each row in the dataset to run 2012- 2019 data through the prediction 
# function, then grab the zip code and save the the 2020 prediction in my helper arrays
for ind in df.index:
    data = [[df['2012_MHI'][ind], df['2013_MHI'][ind], df['2014_MHI'][ind], df['2015_MHI'][ind], df['2016_MHI'][ind], df['2017_MHI'][ind], df['2018_MHI'][ind], df['2019_MHI'][ind]]]
    row = pd.DataFrame(data, columns = ['2012_MHI', '2013_MHI', '2014_MHI', '2015_MHI', '2016_MHI', '2017_MHI', '2018_MHI', '2019_MHI'])
    zips.append(df['zip_code'][ind])
    out.append(prediction(row)[0])

# The helper arrays have the same size and the zip codes coorespond with the 
# 2020 predictions so I combine them into a single dataframe and then grab the 
# zip code coordinates from the coordinates csv. 
df_2020 = pd.DataFrame({'zip_code': zips, '2020_pred': out}, columns=['zip_code', '2020_pred'])
zip_coor = pd.read_csv('https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data')
df_2020 = df_2020.join(zip_coor.set_index('ZIP'), on = 'zip_code').dropna()
df_2020.to_parquet('df_2020.parquet.gzip')

print(df_2020)

