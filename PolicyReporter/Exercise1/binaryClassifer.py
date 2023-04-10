import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def find_threshold(metrics_dict, recall_threshold=0.9):
    """
    Find thresholds with a recall greater than or equal to the given recall_threshold.
    :param metrics_dict: A dictionary containing the threshold as the key and its corresponding confusion matrix values (tp, tn, fp, fn) as the value.
    :param recall_threshold:  recall_threshold (float, optional): The minimum recall value. Defaults to 0.9.
    :return: Yields float Thresholds that satisfy the given recall_threshold.
    """
    if not metrics_dict or not isinstance(metrics_dict, dict):
        return None
    for threshold, metrics in metrics_dict.items():
        tp, tn, fp, fn = metrics
        recalls = tp / (tp + fn)
        if recalls >= recall_threshold:
            yield threshold


def binary_classifier():
    def compute_metrics(y_test, y_probs, thresholds):
        """
        Compute metrics for each threshold.
        :param y_test:  The true labels of the test set.
        :param y_probs: The predicted probabilities for the positive class.
        :param thresholds:  The list of thresholds to evaluate.
        :return:  A dictionary containing the threshold as the key and its corresponding
                  confusion matrix values (tp, tn, fp, fn) as the value.
        """

        metrics_dict = {}
        for threshold in thresholds:
            y_pred = (y_probs >= threshold).astype(int)
            tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
            metrics_dict[threshold] = (tp, tn, fp, fn)
        return metrics_dict

    # Generate synthetic binary classification dataset
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a binary classification model (Logistic Regression)
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)

    # Predict probabilities for the test set
    y_probs = clf.predict_proba(X_test)[:, 1]

    # Define thresholds
    thresholds = np.arange(0.1, 1.0, 0.1)

    # Compute the metrics for each threshold
    metrics_dict = compute_metrics(y_test, y_probs, thresholds)

    # Find the thresholds that yield a recall >= 0.9
    result = list(find_threshold(metrics_dict))

    if result:
        print(f"The thresholds that yield a recall >= 0.9 are: {result}")
    else:
        print("No threshold found that yields a recall >= 0.9")


if __name__ == '__main__':
    binary_classifier()
