import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import os
import time

def train_model():
    train_path = os.path.join("data", "processed", "train.csv")
    test_path = os.path.join("data", "processed", "test.csv")
    model_path = os.path.join("models", "sentiment_model.joblib")
    
    print("Loading data...")
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        
        # Handle NaN values if any (though processing should have removed them)
        train_df = train_df.dropna(subset=['text', 'label'])
        test_df = test_df.dropna(subset=['text', 'label'])
        
        X_train = train_df['text']
        y_train = train_df['label']
        X_test = test_df['text']
        y_test = test_df['label']
        
        print("Defining pipeline...")
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000)),
            ('clf', LogisticRegression(max_iter=1000, solver='lbfgs'))
        ])
        
        # Hyperparameters to tune
        param_grid = {
            'tfidf__ngram_range': [(1, 1), (1, 2)],
            'clf__C': [0.1, 1, 10]
        }
        
        print("Starting Grid Search...")
        grid_search = GridSearchCV(pipeline, param_grid, cv=3, n_jobs=-1, verbose=1)
        
        start_time = time.time()
        grid_search.fit(X_train, y_train)
        training_time = time.time() - start_time
        
        print(f"Training completed in {training_time:.2f} seconds")
        print(f"Best parameters: {grid_search.best_params_}")
        
        best_model = grid_search.best_estimator_
        
        print("Evaluating model...")
        y_pred = best_model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Save model
        joblib.dump(best_model, model_path)
        print(f"Model saved to {model_path}")
        
    except Exception as e:
        print(f"Error training model: {e}")

if __name__ == "__main__":
    train_model()
