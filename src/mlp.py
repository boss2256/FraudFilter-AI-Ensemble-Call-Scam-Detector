import joblib
import numpy as np
from models import get_models, train_and_evaluate_models, save_best_model

# Load the preprocessor and the dataset
preprocessor = joblib.load('data/preprocessor.joblib')
data = np.load('data/train_test_data.npz')
X_train, y_train = data['X_train'], data['y_train']
X_test, y_test = data['X_test'], data['y_test']

# Get models
models = get_models()

# Train and evaluate models
results = train_and_evaluate_models(models, X_train, y_train, X_test, y_test)

# Save the best model based on the evaluation
save_best_model(results, models)
