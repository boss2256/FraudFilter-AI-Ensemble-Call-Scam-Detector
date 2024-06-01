## Project Overview
This project involves the development of a machine learning pipeline to classify phone calls as 'scam' or 'not scam' based on historical call data. The goal is to enhance telecommunications security by identifying and alerting on potential scam calls.

## Folder Structure
```
Jia Jun (project directory)/
│
├── data/
│   ├── calls.db         # The database file with call records.
│   ├── preprocessor.joblib  # Saved preprocessor for data preparation.
│   └── train_test_data.npz   # Saved training and testing datasets.
│
├── src/
│   └── data_access.py            # Python script for acccessing the data.
│   └── data_clean.py            # Python script for data cleaning.
│   └── data_preprocessing.py            # Python script for preprocessing.
│   └── models.py            # Python script for models.
│   └── mlp.py            # Python script for the machine learning pipeline.
│
├── eda.ipynb           # Jupyter notebook for exploratory data analysis.
│
├── README.md          # This file, detailing project setup and execution.
│
├── requirements.txt   # List of project dependencies.
│
└── run.sh              # Bash script to execute the ML pipeline.
```

## Execution Instructions
To run the machine learning pipeline:
1. Ensure Python and necessary packages are installed via `pip install -r requirements.txt`.
2. Activate the environment where dependencies are installed.
3. Execute the script using the command: `./run.sh`.

## Modifications
Parameters within the `mlp.py` can be adjusted to experiment with different modeling techniques or preprocessing steps. These adjustments can be made directly in the `mlp.py` file under the `src/` directory.

## Pipeline Design and Logical Flow
1. **Data Loading:** Data is retrieved from `calls.db` using SQLite.
2. **Data Preprocessing:** Data is cleaned and transformed using a preprocessor saved as `preprocessor.joblib`.
3. **Model Training:** Multiple models are trained and evaluated to determine the most effective at identifying scam calls.
4. **Model Selection and Serialization:** The best-performing model is saved for future use or deployment.

## Key Findings from EDA
- The EDA revealed imbalances in class distribution and identified key features influencing scam call likelihood.
- Feature engineering was employed to enhance model performance, integrating new features based on interactions observed in the data.

## Feature Processing
| Feature                | Processing Steps               |
|------------------------|--------------------------------|
| Call Duration          | Normalized                     |
| Call Frequency         | Normalized                     |
| Financial Loss         | Filled missing, Normalized     |
| Flagged by Carrier     | Encoded, Filled missing values |
| Is International       | Encoded                        |
| Previous Contact Count | Normalized                     |
| Device Battery         | Encoded                        |

## Model Choice and Evaluation
- **Random Forest:** Balanced precision and recall.
- **Gradient Boosting:** High precision, lower recall.
- **Logistic Regression:** Lower performance, particularly in recall.

Models were evaluated based on precision, recall, and F1-score. Random Forest was selected for deployment due to its superior overall performance.

## Model Evaluation Results

### Random Forest Model Evaluation

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.86      | 0.94   | 0.90     | 1511    |
| 1     | 0.88      | 0.73   | 0.80     | 889     |
| Accuracy | 0.86 | - | - | 2400 |
| Macro Avg | 0.87 | 0.84 | 0.85 | 2400 |
| Weighted Avg | 0.86 | 0.86 | 0.86 | 2400 |

### Gradient Boosting Model Evaluation

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.81      | 0.99   | 0.89     | 1511    |
| 1     | 0.98      | 0.60   | 0.74     | 889     |
| Accuracy | 0.85 | - | - | 2400 |
| Macro Avg | 0.89 | 0.80 | 0.82 | 2400 |
| Weighted Avg | 0.87 | 0.85 | 0.84 | 2400 |

### Logistic Regression Model Evaluation

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.78      | 0.96   | 0.86     | 1511    |
| 1     | 0.89      | 0.53   | 0.66     | 889     |
| Accuracy | 0.80 | - | - | 2400 |
| Macro Avg | 0.83 | 0.74 | 0.76 | 2400 |
| Weighted Avg | 0.82 | 0.80 | 0.79 | 2400 |


## Deployment Considerations
- Ensure consistent environment setup for deployment.
- Monitor model performance over time to detect drift.
- Consider re-training the model with new data periodically to maintain its effectiveness.

