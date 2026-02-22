import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

class HousePriceModel:

    def __init__(self, file_path):
        self.file_path = file_path
        self.model = LinearRegression()
        self.data = None
        self.X = None
        self.y = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

        # Basic features
        self.X = self.data[['sqft_living', 'bedrooms', 'bathrooms']]
        self.y = self.data['price']

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)

        print("Model trained successfully")
        print("Mean Absolute Error:", mae)

    def predict(self, sqft, bedrooms, bathrooms):
        input_data = pd.DataFrame(
            [[sqft, bedrooms, bathrooms]],
            columns=['sqft_living', 'bedrooms', 'bathrooms']
        )

        prediction = self.model.predict(input_data)
        return prediction[0]