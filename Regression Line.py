import numpy as np
import matplotlib.pyplot as plt

# The predicted value is marked in the plot as a red dot

file = "/desktop/inputdata6.csv"

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
    
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  
    return (b_0, b_1)
  
def plot_regression_line(x, y, b):

    # plotting the actual points as scatter plot
    plt.figure(figsize=(20,10))
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
    

    # predicted response vector
    y_pred = b[0] + b[1]*x
  
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
  
    # putting labels
    plt.xlabel("Rainfall")
    plt.ylabel("Productivity")
    plt.title("Scatter Plot:Rainfall vs Productivity ")

    # Plot the productivity coefficient value for 245mm precipitation
    z = np.interp(245, x,y_pred)
    plt.plot(245,z,marker='.',c = 'red', ls='none', ms=20)
  
    # function to show plot 
    plt.grid()
    plt.show()

    print("Productivity Coefficient for 245mm Precipitation: ", z)
  
def main():

    File_data = np.loadtxt(file, dtype=str,skiprows=1)

    # observations / data
    x3 = [i[0] for i in File_data]
    x2 = [s.strip('.,') for s in x3]
    x1 = [float(numeric_string) for numeric_string in x2]
    x = np.asarray(x1)
  
    y2 = [i[1] for i in File_data]
    y1 = [float(numeric_string) for numeric_string in y2]
    y = np.asarray(y1)
  
    # estimating coefficients
    b = estimate_coef(x, y)
  
    # plotting regression line
    plot_regression_line(x, y, b)

main()