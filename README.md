# RXA_assignment

The goal of this exercise was to take a csv of median household incomes by zip codes (2011-2019) and create a project from this. In order to do this I had to clean the data, analyze the data and then derive value from the data in the form of a project. 

1. The first thing done was cleaning the data. After briefly looking at the data I noticed negative numbers and 0 in spots they didn't belong. I looped through the entire set and either got rid of the rows with incomplete data (for Machine Learning) or turned these values into NaN values (for map plotting). 

2. The second thing I did was create a machine learning model. I decided on linear regression for the model because I wanted to understand the relationship between time and median income in certain areas, then use this relationship to forecast median incomes for the future. After training and testing the model, I found the explained variance to be .955, which indicates a correlation between time and median household income. Pairing that with the mean absolute error of 3397.18, which means on average the model was around 3000 dollars wrong, I felt comfortable doing my forecasts with this model. 

3. The third thing I did was use my machine learning model to forecast the median household income of each zip code for 2020.

4. The fourth and final thing I did was create a Dashboard for exploring the data. The first tab was created to show the median household income color coded and plotted at each zip code for users to see income disparencies across the United States and throughout time. This plotted map also included the projections for 2020. The second tab includes a paginated table showing the zip codes and their median household incomes from 2011-2019 for users to look up specific zip codes easier. The third and final tab included a calculator that uses the machine learning model to predict the next years income, based on the input data. 

The technology and libraries used in creation of this project was as followed:

* Python as the main programming language
* Pandas for data manipulation 
* Plotly for visualization 
* Dash to create the web interface 
* Sklearn for machine learning 
* Docker to containerize my project 
* Bash scripts to make building and running the project simplier 

# To Build and Run my project
# With Docker 
(inside the project directory)
1. run 'sh build.sh' - to build the docker image
2. run 'sh run.sh' - to run the project in a docker container 
3. You can then see the web interface at http://0.0.0.0:8050

# Without Docker 
(inside the project directory)
1. run 'pip install -r requirements.txt'- This will install all the required libraries for this project 
2. run 'python3 app.py'- This will start the web interface at http://0.0.0.0:8050




