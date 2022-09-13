import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, mean_absolute_error
from sklearn.model_selection import train_test_split

# I begin by opening up the machine learning data frame and dropping an leftover NaN values
df = pd.read_parquet('df_ml.parquet.gzip')
df = df.dropna()

# I then split the original data into a test set and train set
train, test = train_test_split(df)

# The train and test sets are then broken into input and output data sets
inputs = ['2011_MHI', '2012_MHI', '2013_MHI', '2014_MHI', '2015_MHI', '2016_MHI', '2017_MHI', '2018_MHI']
df_train_in = train[inputs]
df_train_out = train['2019_MHI']
df_test_in = test[inputs]
df_test_out = test['2019_MHI']

# The model is instantiated and trained using the training inputs and outputs
model = LinearRegression()
model.fit(df_train_in, df_train_out)

# I then create a function that will take a data frame and run it throught the model
def prediction(df):
    pred = model.predict(df)
    return pred

# Below I ran the test data through the model and found the explained variance 
# and the mean absolute error

#pred = prediction(df_test_in)

#print('Linear Regression Results')
#print('Explained Variance: '+str(explained_variance_score(df_test_out, pred)))
#print('Mean Absolute Error: ' + str(mean_absolute_error(df_test_out, pred)))

# Linear Regression Results- .955
# Mean Absolute Error- 3397.18