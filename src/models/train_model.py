import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import os
import time
from pathlib import Path


def train_model():
    """
    Trains sentiment model with GridSearch
    """
    # Paths relative to project
    project_root = Path(__file__).parent.parent.parent
    train_path = project_root / "data" / "processed" / "train.csv"
    test_path = project_root / "data" / "processed" / "test.csv"
    model_path = project_root / "models" / "sentiment_model.joblib"

    # Create models directory if needed
    model_path.parent.mkdir(parents=True, exist_ok=True)

    print("Loading data...")
    try:
        if not train_path.exists() or not test_path.exists():
            print("Error: Train/test files not found!")
            print("Run first:")
            print("  python src/data/download_data.py")
            print("  python src/data/process_data.py")
            return

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        print(f"Train: {len(train_df)} samples")
        print(f"Test: {len(test_df)} samples")

        # Remove NaN (normally already done but we check)
        train_df = train_df.dropna(subset=["text", "label"])
        test_df = test_df.dropna(subset=["text", "label"])

        X_train = train_df["text"]
        y_train = train_df["label"]
        X_test = test_df["text"]
        y_test = test_df["label"]

        # Check that labels are -1, 0, 1
        print(f"Unique train labels: {sorted(y_train.unique())}")

        print("Creating pipeline...")
        # Pipeline: TF-IDF + Logistic Regression
        pipeline = Pipeline(
            [
                ("tfidf", TfidfVectorizer(max_features=5000, stop_words="english")),
                (
                    "clf",
                    LogisticRegression(max_iter=1000, solver="lbfgs", random_state=42),
                ),
            ]
        )

        # Hyperparameters for GridSearch
        # TODO: Maybe try other parameters?
        param_grid = {
            "tfidf__ngram_range": [(1, 1), (1, 2)],  # unigrams or bigrams
            "clf__C": [0.1, 1, 10],  # regularization
        }

        print("Starting Grid Search (this may take a while)...")
        grid_search = GridSearchCV(
            pipeline,
            param_grid,
            cv=3,  # 3-fold cross-validation
            n_jobs=-1,
            verbose=1,
            scoring="accuracy",
        )

        start_time = time.time()
        grid_search.fit(X_train, y_train)
        training_time = time.time() - start_time

        print(f"\nTraining completed in {training_time:.2f} seconds")
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")

        best_model = grid_search.best_estimator_

        # Evaluate on test set
        print("\nEvaluating on test set...")
        y_pred = best_model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy:.4f}")

        print("\nClassification report:")
        print(classification_report(y_test, y_pred))

        # Confusion matrix (optional, for debugging)
        # cm = confusion_matrix(y_test, y_pred)
        # print("\nConfusion matrix:")
        # print(cm)

        # Save model
        joblib.dump(best_model, model_path)
        print(f"\nModel saved to {model_path}")

    except Exception as e:
        print(f"Error during training: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    train_model()
