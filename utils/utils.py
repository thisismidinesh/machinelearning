# Utility functions for machine learning project

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report

def load_data(filepath):
    """Load data from CSV file."""
    return pd.read_csv(filepath)

def save_model(model, filepath):
    """Save model using joblib."""
    import joblib
    joblib.dump(model, filepath)

def load_model(filepath):
    """Load model using joblib."""
    import joblib
    return joblib.load(filepath)

def evaluate_model(y_true, y_pred):
    """Evaluate model performance."""
    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)
    return acc, report