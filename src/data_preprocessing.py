import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import numpy as np


def preprocess_data(data):
    categorical_cols = ['Is International', 'Flagged by Carrier', 'Call Type', 'Device Battery']
    numerical_cols = ['Call Duration', 'Call Frequency', 'Financial Loss', 'Previous Contact Count']

    # Create a transformer pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(), categorical_cols)
        ])

    # Split data into features and target
    X = data.drop('Scam Call', axis=1)  # Adjust depending on your label column
    y = data['Scam Call'].apply(lambda x: 1 if x == 'Scam' else 0)

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the preprocessor and transform the training data
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)

    # Save the preprocessor and the transformed data
    joblib.dump(preprocessor, 'data/preprocessor.joblib')
    np.savez('data/train_test_data.npz', X_train=X_train_transformed, y_train=y_train, X_test=X_test_transformed,
             y_test=y_test)

    return X_train_transformed, X_test_transformed, y_train, y_test
