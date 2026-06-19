import random
# Define a function to split x and y into train and test sets
def train_test_split(x, y, test_size=0.2):
    # We need to shuffle the data to avoid any bias in the split
    # Combine the x and y values into tuples (pairs) so they stay together after shuffling
    combined = []
    for i in range(len(x)):
        combined.append((x[i], y[i]))

    # Shuffle the combined list randomly
    random.shuffle(combined)

    # Find the index at which to split the list into training and testing sets
    test_count = int(len(combined) * test_size)
    split_index = len(combined) - test_count

    # Create the training set by taking the first part of the shuffled list
    train_data = combined[:split_index]

    # Create the testing set by taking the remaining part of the shuffled list
    test_data = combined[split_index:]

    # Create empty lists to hold separated x and y values for the training set
    x_train = []
    y_train = []

    # Fill x_train and y_train by looping through each pair in the training set
    for pair in train_data:
        x_train.append(pair[0])
        y_train.append(pair[1])
    
    # Create empty lists to hold separated x and y values for the testing set
    x_test = []
    y_test = []

    # Fill x_test and y_test by looping through each pair in the testing set
    for pair in test_data:
        x_test.append(pair[0])
        y_test.append(pair[1])
    
    # Return the four lists: x_train, x_test, y_train, y_test
    return x_train, x_test, y_train, y_test


def data_summary(values):
    # Do the computations with simple native python computations
    # Total number of values
    count = len(values)
    
    # Sum of values
    total = sum(values)
    
    # Mean, maximum and minimum
    if(count==0):
        mean=None
        minimum=None
        maximum=None
        print('Invalid values since the sum is zero')
    else:
        mean = total / count
        minimum = min(values)
        maximum = max(values)
    
    # Sorted values for median
    sorted_vals = sorted(values)
    
    # Median
    if count == 0:
        median = None
    elif count % 2 == 1:
        median = sorted_vals[count // 2]
    else:
        median = (sorted_vals[count // 2 - 1] + sorted_vals[count // 2]) / 2
    
    # Return results as dictionary
    return {
        "count": count,
        "sum": total,
        "mean": mean,
        "min": minimum,
        "max": maximum,
        "median": median
    }