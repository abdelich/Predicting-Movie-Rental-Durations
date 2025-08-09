# Predicting-Movie-Rental-Durations

Time to put your regression knowledge to the test! A DVD rental company has approached you to make a regression model which will help predict the number of days a customer rents a DVD. The model will hopefully make their inventory planning much more efficient. You decide to help them by running some regression models and recommending the best-performing model to the company.





A DVD rental company needs your help! They want to figure out how many days a customer will rent a DVD for based on some features and has approached you for help. They want you to try out some regression models which will help predict the number of days a customer will rent a DVD for. The company wants a model which yeilds a MSE of 3 or less on a test set. The model you make will help the company become more efficient inventory planning.



The data they provided is in the csv file `rental\_info.csv`. It has the following features:

\- `"rental\_date"`: The date (and time) the customer rents the DVD.

\- `"return\_date"`: The date (and time) the customer returns the DVD.

\- `"amount"`: The amount paid by the customer for renting the DVD.

\- `"amount\_2"`: The square of `"amount"`.

\- `"rental\_rate"`: The rate at which the DVD is rented for.

\- `"rental\_rate\_2"`: The square of `"rental\_rate"`.

\- `"release\_year"`: The year the movie being rented was released.

\- `"length"`: Lenght of the movie being rented, in minuites.

\- `"length\_2"`: The square of `"length"`.

\- `"replacement\_cost"`: The amount it will cost the company to replace the DVD.

\- `"special\_features"`: Any special features, for example trailers/deleted scenes that the DVD also has.

\- `"NC-17"`, `"PG"`, `"PG-13"`, `"R"`: These columns are dummy variables of the rating of the movie. It takes the value 1 if the move is rated as the column name and 0 otherwise. For your convinience, the reference dummy has already been dropped.


MSE = 2.23

