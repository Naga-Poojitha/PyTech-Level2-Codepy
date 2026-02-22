import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


class PassFailModel:

    def __init__(self, file_path):
        self.file_path = file_path
        self.model = LogisticRegression()
        self.data = None
        self.X = None
        self.y = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

        # Create average column
        self.data['average'] = (
            self.data['math score'] +
            self.data['reading score'] +
            self.data['writing score']
        ) / 3

        # Create target column with proper academic rule
        self.data['result'] = self.data.apply(
            lambda row: 1
            if (
                row['math score'] >= 35 and
                row['reading score'] >= 35 and
                row['writing score'] >= 35 and
                row['average'] >= 40
            )
            else 0,
            axis=1
        )

        # Features and target
        self.X = self.data[['math score', 'reading score', 'writing score']]
        self.y = self.data['result']

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )

        print(f"Training samples: {len(X_train)}")
        print(f"Testing samples: {len(X_test)}")

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        # Confusion Matrix
        cm = confusion_matrix(y_test, predictions)
        print("\nConfusion Matrix:")
        print(cm)

        return accuracy_score(y_test, predictions)

    def predict(self, math, reading, writing):

        # Rule-based academic check
        average = (math + reading + writing) / 3

        if (
            math < 35 or
            reading < 35 or
            writing < 35 or
            average < 40
        ):
            return "Fail"

        # ML prediction
        input_data = pd.DataFrame(
            [[math, reading, writing]],
            columns=['math score', 'reading score', 'writing score']
        )

        result = self.model.predict(input_data)

        return "Pass" if result[0] == 1 else "Fail"

    def get_trained_model(self):
        return self.model