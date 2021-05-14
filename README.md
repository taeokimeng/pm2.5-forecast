# PM2.5 Forecast with LSTM

For a PM2.5 forecast, LSTM is used.
Data could be stored in database, and we might need to access data from database and save it in database.
There are some examples to handle PostgreSQL and SQLite3.
You can catch up with the examples to use PostgreSQL or SQLite3.

## Further more
PM2.5 data could be stored or appended in database.
The architecture could be:
1. Load data from database.
2. Send the data and request predictions by using TensorFlow Serving with RESTful API.
3. Store the predictions in database and show it on frontend.
