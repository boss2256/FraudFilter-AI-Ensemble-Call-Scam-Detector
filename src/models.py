from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

def get_models():
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'Logistic Regression': LogisticRegression(max_iter=300, random_state=42)
    }
    return models

def train_and_evaluate_models(models, X_train, y_train, X_test, y_test):
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        report = classification_report(y_test, predictions, output_dict=True)
        results[name] = report
        print(f"{name} model evaluation:")
        print(classification_report(y_test, predictions))
    return results

def save_best_model(results, models):
    best_model_name = max(results, key=lambda x: results[x]['1']['f1-score'])
    best_model = models[best_model_name]
    joblib.dump(best_model, 'data/best_model.joblib')
