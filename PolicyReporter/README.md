## Exercise 1 

The implementation can be find in `Exercise1.ipynb`. 
```python
def find_threshold(metrics_dict, recall_threshold=0.9):
    """
    Find thresholds with a recall greater than or equal to the given recall_threshold.
    :param metrics_dict: A dictionary containing the threshold as the key and its corresponding confusion matrix values (tp, tn, fp, fn) as the value.
    :param recall_threshold:  recall_threshold (float, optional): The minimum recall value. Defaults to 0.9.
    :return: Yields float Thresholds that satisfy the given recall_threshold.
    """
    if not metrics_dict:
        return None
    for threshold, metrics in metrics_dict.items():
        tp, tn, fp, fn = metrics
        recalls = tp / (tp + fn)
        if recalls >= recall_threshold:
            yield threshold
```
### Demo

A demo has been implemented to showcase the usage of custom recall threshold in a binary classification model in `Exercise1.ipynb`.

### Design Document: Binary Classification with Custom Recall Threshold

1. Overview
The goal of this project is to develop a binary classification model that achieves a recall value greater than or equal to a specified threshold. The model will be trained on a synthetic dataset generated using the make_classification function from the scikit-learn library. The model will be a logistic regression model, and we will use custom functions to compute the metrics for each threshold and find the optimal threshold for the desired recall.

2. Dataset
Dataset: Synthetic binary classification dataset
Source: Scikit-learn's make_classification function
Preprocessing: None
3. Model
Model: Logistic Regression
Hyperparameters: random_state=42
Training: train_test_split
4. Evaluation
Custom compute_metrics function to calculate confusion matrix values for each threshold
Custom find_threshold function to find the threshold with a recall greater than or equal to the specified threshold
5. Implementation Plan

6. Generate a synthetic binary classification dataset using the make_classification function.

7. Split the dataset into training and testing sets using train_test_split.

8. Train a logistic regression model on the training set.

9. Predict probabilities for the test set using the trained model.

10. Define custom compute_metrics and find_threshold functions.

11. Compute the metrics for each threshold using the compute_metrics function.

12. Find the thresholds that yield a recall greater than or equal to 0.9 using the find_threshold function.

13. Pseudocode
```
1. Generate synthetic binary classification dataset
2. Split the dataset into training and testing sets
3. Train a logistic regression model on the training set
4. Predict probabilities for the test set
5. Define custom compute_metrics function
6. Define custom find_threshold function
7. Compute metrics for each threshold
8. Find the thresholds that yield a recall greater than or equal to 0.9
```


## Exercise 2 
### Design Document: Module Name: Finite State Machine (FSM) Library
##### Introduction
This design document covers the implementation details of a Finite State Machine (FSM) library that is versatile and easy to use. The primary use case for this library is to implement a modulo-three function that computes the remainder when an unsigned binary integer is divided by three. However, the library can be extended to accommodate other use cases as well.

##### Components
The FSM library consists of the following components:

    Character
    Alphabet
    StateInterface
    State
    FinalState
    States
    Transition
    Transitions
    Builder
    FSMInterface
    ModThreeFSM
##### Component Descriptions
1. Character
   Represents a single character in the alphabet.
   Provides a way to compare characters for equality.
   The symbol attribute holds the character value.
2. Alphabet
   Represents the input alphabet for the finite state machine.
   Maintains a set of Character instances.
   The is_valid method checks if a given input symbol is a valid character in the alphabet.
3. StateInterface (Abstract Base Class)
   Serves as the base class for different types of states in the finite state machine.
   Enforces the implementation of a common interface for all state types.
4. State
   Represents a non-final state in the finite state machine.
   Inherits from the StateInterface class. Not being used in this exercise since all states are final state.
5. FinalState
   Represents a final state in the finite state machine.
   Inherits from the StateInterface class.
6. States
   A collection of states for the finite state machine.
   Stores states in a dictionary with their names as keys.
   The get_state method retrieves a state object by its name.
7. Transition
   Represents a state transition in the finite state machine.
   Stores the origin state, input symbol, and destination state.
8. Transitions
   A collection of transitions for the finite state machine.
   Stores transitions in a dictionary with tuples of (origin state, input symbol) as keys and destination states as values.
   The get_next_state method retrieves the next state based on the current state and input symbol.
9. Builder
   A Builder class for constructing the finite state machine.
   Provides methods to set the alphabet, states, transitions, and initial state.
   The build method returns an instance of the FSM implementation (e.g., ModThreeFSM).
10. FSMInterface (Abstract Base Class)
    Serves as the base class for the finite state machine implementation.
    Enforces the implementation of a common interface for all FSM implementations.
11. ModThreeFSM
    The modulo-3 finite state machine implementation.
    Inherits from the FSMInterface class.
    The process_input method processes an input string and returns True if the input string is accepted by the FSM.
##### Usage
To use the FSM library for the modulo-3 function, follow these steps:

1. Define the characters, alphabet, states, and transitions.
2. Create a Builder instance and set the alphabet, states, and transitions.
3. Build the ModThreeFSM instance using the builder and set the initial state.
4. Process an input string using the ModThreeFSM.process_input method.

##### Demo
Examples of usage can be find in `mod-three.py` file:

    The input string '1101' has remainder: 1
    The input string '1110' has remainder: 2
    The input string '1111' has remainder: 0
    The input string '1110010011111001110011000' has remainder: 0

Testing
Unit tests are provided for each class in the FSM library. The unittest library is used to write and run