# Import libraries

import numpy as np 
import matplotlib.pyplot as plt

# Analyzing funtions

def analyzefunction(x, primitive, derivative1, derivative2):
    try:
        y = eval(primitive)
        y1 = eval(derivative1)
        y2 = eval(derivative2)
    except Exception as e:
        print("Error:", e)
        return

    # Plotting graphs

    plt.figure(figsize=(7, 5))
    plt.plot(x, y, color='yellow', label='f(x)')
    plt.plot(x, y1, color='orange', label="f'(x)")
    plt.plot(x, y2, color='purple', label="f''(x)")
    plt.title("Functions")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Formulas for tests

tests = {
    '1': {
        
        'f': "np.exp(np.sin(x**2)) / np.exp(x**2)",
        'f1': "2*x*(np.cos(x**2)-1)*np.exp(np.sin(x**2)-x**2)",
        'f2': (
            "2*(np.cos(x**2)-1)*np.exp(np.sin(x**2)-x**2) "
            "- 2*x*(np.sin(x**2)*2*x)*np.exp(np.sin(x**2)-x**2) "
            "+ 2*x*(np.cos(x**2)-1)*np.exp(np.sin(x**2)-x**2)*(np.cos(x**2)*2*x - 2*x)"
        )
    },
    '2': {
        
        'f': "np.exp(np.cos(x**2)) / np.exp(x**2)",
        'f1': "np.exp(np.cos(x**2) - x**2) * (-2 * x * (np.sin(x**2) + 1))",
        'f2': (
            "np.exp(np.cos(x**2) - x**2) * "
            "(4 * x**2 * (np.sin(x**2) + 1)**2 - 2 * (np.sin(x**2) + 1) - 4 * x**2 * np.cos(x**2))"
        )
    },
    '3': {
        
        'f': "np.exp(np.sin(x)) / np.exp(x)",
        'f1': "np.exp(np.sin(x) - x) * (np.cos(x) - 1)",
        'f2': "np.exp(np.sin(x) - x) * ((np.cos(x) - 1)**2 - np.sin(x))"
    }
}

# Main cycle
while True:

# User selects a test
    test = input('What test to choose: 1, 2 or 3?\t')

    if test not in tests: # if user typed a wrong number an error message appears
        print("Error, please choose 1, 2 or 3.")
        continue

# User chooses an interval and a number of points
    try:
        start = float(input("Enter interval start point: "))
        end = float(input("Enter interval end point: "))
        num_points = int(input("Enter number of points: "))
        if num_points <= 1: # User should choose more than 1 point
            raise ValueError("Number of points must be more than 1.")
        if start >= end: # User should choose the start point value that is smaller than end point value
            raise ValueError("Start point value should be smaller than end point value.")
    except ValueError as e:
            print(f"Error: {e}")
            continue


# Plotting the X-axis
    x = np.linspace(start, end, num_points)
    params = tests[test]
    analyzefunction(x, params['f'], params['f1'], params['f2'])

    # Asking if user wants to continue testing (nested cycle)
    while True:
        again = input("Want to test more? (y/n): ").strip().lower()
        if again == 'y':
            break  # we exit the nested cycle and run the main cycle again
        elif again == 'n':
            print("Okey, bye!")
            exit()
        else:
            print("Error: enter 'y' (for YES) or 'n' (for NO).")