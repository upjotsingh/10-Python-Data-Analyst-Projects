# from mini_regression/module.py import fit

from mini_regression.model import fit_regression,predict_regression,compute_residuals
from mini_regression.utils import train_test_split,data_summary

def main():
    # Initialize data
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [3, 6, 9, 12, 15, 18, 21, 24, 27, 55]


    # Print X and Y to check the data
    print('\nX values',X)
    print('Y values',Y)


    # Call the fit_regression function
    # and store the returned slope (m) and intercept (b)
    m,b=fit_regression(X,Y)
    print('\nSlope (m)',m)
    print('Intercept (b)',b)

    # call the predict_regression function
    # and store the returned list of predicted y-values
    y_pred_values=predict_regression(X,m,b)
    print("\nPredicted Y values: ",y_pred_values)
   

    #Call the compute_residuals function
    #and store the returned list of residuals
    residuals=compute_residuals(Y,y_pred_values)
    print('\nResiduals: ',residuals)

    # Splitting data into test and train
    x_train, x_test, y_train, y_test=train_test_split(X,Y)
    print('\nX train: ',x_train,"\nX Test: ",x_test,"\nY Train: ",y_train,"\nY Test: ",y_test)
    
    # Fetching data summary
    xTrainSummary=data_summary(x_train)
    yTrainSummary=data_summary(y_train)
    print('\nSummary for X_Train data', xTrainSummary)
    print('\nSummary for Y_Train data', yTrainSummary)


if __name__ == "__main__":
    main()