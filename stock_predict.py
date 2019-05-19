import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import quandl
import datetime
style.use('ggplot')

#Dates
start_date = datetime.date(2017,1,3)
end_date = datetime.date.today()

quandl.ApiConfig.api_key = <API KEY here>

#Get Data From Quandl
df = quandl.get('WIKI/GOOGL', start_date=start_date, end_date=end_date, collapse="daily")
df = df.reset_index()
prices = df['Close'].tolist()
dates = df.index.tolist()

#Convert to 1d Vector
dates = np.reshape(dates, (len(dates), 1))
prices = np.reshape(prices, (len(prices), 1))

print(dates[:5])


#Define Linear Regressor Object
regressor = LinearRegression()
regressor.fit(dates, prices)
 
#Visualize Results
plt.scatter(dates, prices, color='yellow', label= 'Actual Price') #plotting the initial datapoints
plt.plot(dates, regressor.predict(dates), color='red', linewidth=3, label = 'Predicted Price') #plotting the line made by linear regression
plt.title('Linear Regression | Time vs. Price')
plt.legend()
plt.xlabel('Date Integer')
plt.show()
 
#Predict Price on Given Date
date = [[15]]
predicted_price =regressor.predict(date)
print("Predicted Price is ",predicted_price[0][0],"with regression coeff and intercept as follows: ",regressor.coef_[0][0] ,regressor.intercept_[0])