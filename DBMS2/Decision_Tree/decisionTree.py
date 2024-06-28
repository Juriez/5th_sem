import numpy as np
import pandas as pd
import seaborn as sns
import random
from sklearn.model_selection import KFold

# Load the iris dataset
iris = sns.load_dataset("iris")
# print(iris)
# Function to check purity
def check_purity(data):
    label_column = data[:, -1]
    unique_classes = np.unique(label_column)
    if len(unique_classes) == 1:
        return True
    return False

# Function to classify data
def classify_data(data):
    label_column = data[:, -1]
    unique_classes, counts_unique_classes = np.unique(label_column, return_counts=True)
    classification = unique_classes[counts_unique_classes.argmax()]
    return classification

# Function to get potential splits
def get_potential_splits(data):
    potential_splits = {}
    _, n_columns = data.shape
    for column_index in range(n_columns - 1):
        potential_splits[column_index] = []
        values = data[:, column_index]
        unique_values = np.unique(values)
        for index in range(len(unique_values)):
            if index != 0:
                current_value = unique_values[index]
                previous_value = unique_values[index - 1]
                potential_split = (current_value + previous_value) / 2
                potential_splits[column_index].append(potential_split)
    return potential_splits

# Function to split data
def split_data(data, split_column, split_value):
    split_column_values = data[:, split_column]
    data_below = data[split_column_values <= split_value]
    data_above = data[split_column_values > split_value]
    return data_below, data_above

# Function to calculate entropy
def calculate_entropy(data):
    label_column = data[:, -1]
    _, counts = np.unique(label_column, return_counts=True)
    probabilities = counts / counts.sum()
    entropy = sum(probabilities * -np.log2(probabilities))
    return entropy

# Function to calculate overall entropy
def calculate_overall_entropy(data_below, data_above):
    n = len(data_below) + len(data_above)
    p_data_below = len(data_below) / n
    p_data_above = len(data_above) / n
    overall_entropy = (p_data_below * calculate_entropy(data_below) + p_data_above * calculate_entropy(data_above))
    return overall_entropy

# Function to determine the best split
def determine_best_split(data, potential_splits):
    overall_entropy = 999
    for column_index in potential_splits:
        for value in potential_splits[column_index]:
            data_below, data_above = split_data(data, split_column=column_index, split_value=value)
            current_overall_entropy = calculate_overall_entropy(data_below, data_above)
            if current_overall_entropy <= overall_entropy:
                overall_entropy = current_overall_entropy
                best_split_column = column_index
                best_split_value = value
    return best_split_column, best_split_value

# Decision tree algorithm
def decision_tree_algorithm(df, counter=0, min_samples=2, max_depth=5):
    if counter == 0:
        global COLUMN_HEADERS
        COLUMN_HEADERS = df.columns
        data = df.values
    else:
        data = df
        
    if (check_purity(data)) or (len(data) < min_samples) or (counter == max_depth):
        classification = classify_data(data)
        return classification
    else:
        counter += 1
        potential_splits = get_potential_splits(data)
        split_column, split_value = determine_best_split(data, potential_splits)
        data_below, data_above = split_data(data, split_column, split_value)
        feature_name = COLUMN_HEADERS[split_column]
        question = "{} <= {}".format(feature_name, split_value)
        sub_tree = {question: []}
        yes_answer = decision_tree_algorithm(data_below, counter, min_samples, max_depth)
        no_answer = decision_tree_algorithm(data_above, counter, min_samples, max_depth)
        if yes_answer == no_answer:
            sub_tree = yes_answer
        else:
            sub_tree[question].append(yes_answer)
            sub_tree[question].append(no_answer)
        return sub_tree

# Function to classify examples
def classify_example(example, tree):
    question = list(tree.keys())[0]
    feature_name, comparison_operator, value = question.split()
    if example[feature_name] <= float(value):
        answer = tree[question][0]
    else:
        answer = tree[question][1]
    if not isinstance(answer, dict):
        return answer
    else:
        residual_tree = answer
        return classify_example(example, residual_tree)

# Updated function to calculate accuracy
def calculate_accuracy(df, tree):
    df = df.copy()  # Ensure a copy of the DataFrame is used
    df["classification"] = df.apply(classify_example, axis=1, args=(tree,))
    df["classification_correct"] = df["classification"] == df["species"]
    accuracy = df["classification_correct"].mean()
    return accuracy

# k-Fold Cross-Validation
def k_fold_cross_validation(dataframe, k):
    kf = KFold(n_splits=k, shuffle=True)  # No fixed random_state
    accuracies = []
    
    for train_index, test_index in kf.split(dataframe):
        train_df = dataframe.iloc[train_index]
        test_df = dataframe.iloc[test_index]
        
        tree = decision_tree_algorithm(train_df, max_depth=3)
        accuracy = calculate_accuracy(test_df, tree)
        accuracies.append(accuracy)
        print(accuracy)
    
    average_accuracy = np.mean(accuracies)
    print(f"Average accuracy over {k} folds: {average_accuracy * 100:.2f}%")
    
def testing(example, tree):
    question = list(tree.keys())[0]
    feature_name, comparison_operator, value = question.split()

    # check for answer
    if example[COLUMN_HEADERS.get_loc(feature_name)] <= float(value):
        answer = tree[question][0]
    else:
        answer = tree[question][1]

    # base case
    if not isinstance(answer, dict):
        return answer
    # recursive part
    else:
        residual_tree = answer
        return testing(example, residual_tree)

def get_input_features():
    input_features = []
    for i in range(len(COLUMN_HEADERS) - 1):  # Exclude the last column (species)
        feature_name = COLUMN_HEADERS[i]
        value = float(input("Enter value for {}: ".format(feature_name)))
        input_features.append(value)
    return input_features

k = 5
average_accuracy = k_fold_cross_validation(iris, k)
