def fit_regression(x, y):
    # Calculate the number of points (n)
    n=len(x)
    # Calculate the mean of x and y
    xMean=sum(x)/n
    yMean=sum(y)/n
    
    # Calculate the numerator and denominator for the slope (m)

    numerator=0
    denominator=0

    for i in range(n):
        numerator+=(x[i] - xMean) * (y[i] - yMean)
        denominator+=(x[i] - xMean)**2
    
    # Check if the denominator is zero to avoid division by zero
    if denominator==0:
        print("Error: all x values are the same. Cannot compute slope.")
        return None,None
    
    # Calculate the slope (m) and intercept (b)
    m= numerator/denominator
    b=yMean-m*yMean
    
    # Return both slope and intercept
    return m,b



def predict_regression(x_values, m, b):
    # Create an empty list to store the predicted y-values
    y_pred_values=[]
    
    # Loop through each x in the list of x_values
    # For each x, calculate the predicted y using the formula y = m*x + b
    # Add each predicted y-value to the list
    for x in x_values:
        y=m*x+b
        y_pred_values.append(y)
    
    # Return the list of all predicted y-values
    return y_pred_values

def compute_residuals(y_true, y_pred):
    # Create an empty list to store residuals
    residuals=[]
    
    # Loop through each index in the range of y_true
    # For each index, calculate the residual as (actual y - predicted y)
    # Add each residual to the list
    for i in range(len(y_true)):
        residual=y_true[i] - y_pred[i]
        residuals.append(residual)
 
    
    # Return the list of residuals
    return residuals
