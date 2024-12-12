# carlos hernandez & jonathan nunez

import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

class MyDecisionTreeClassifier:
    def __init__(self):
        self.read_csv_and_split_data()

    def read_csv_and_split_data(self):
        self.data = pd.read_csv("data/weather_classification_data.csv")
        X = self.data.drop('Weather Type', axis=1)
        y = self.data['Weather Type']

        dt_cloudCover = LabelEncoder()
        dt_season = LabelEncoder()
        dt_location = LabelEncoder()

        X['Cloud Cover'] = dt_cloudCover.fit_transform(X['Cloud Cover'])
        X['Season'] = dt_season.fit_transform(X['Season'])
        X['Location'] = dt_location.fit_transform(X['Location'])

        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

        joblib.dump(dt_cloudCover, 'dt_cloudCover.pkl')
        joblib.dump(dt_season, 'dt_season.pkl')
        joblib.dump(dt_location, 'dt_location.pkl')
        joblib.dump(label_encoder, 'dt_label_encoder.pkl')
        self.label_encoder = label_encoder

    def train_and_predict(self):
        self.model = DecisionTreeClassifier()
        self.model.fit(self.X_train, self.Y_train)

        Y_test_pred = self.model.predict(self.X_test)
        Y_train_pred = self.model.predict(self.X_train)
        
        test_accuracy = accuracy_score(self.Y_test, Y_test_pred)
        print("Accuracy Score - Test: ", test_accuracy)

        train_accuracy = accuracy_score(self.Y_train, Y_train_pred)
        print("Accuracy Score - Train: ", train_accuracy)

        joblib.dump(self.model, 'dt_model.pkl')

        plt.figure(figsize=(20,10))
        plot_tree(self.model, filled=True, feature_names=self.data.columns[:-1], class_names=self.label_encoder.classes_)
        plt.title("Decision Tree")
        plt.show()

if __name__ == "__main__":
    decision_tree = MyDecisionTreeClassifier()
    decision_tree.train_and_predict()
