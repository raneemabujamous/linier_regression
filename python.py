import pandas as pd
import matplotlib.pyplot as plt
# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie','Alice', 'Bob', 'Charlie','Alice', 'Bob', 'Charlie','Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22,45, 76, 21,24, 34, 42,25, 32, 43],
        'City': ['New York', 'San Francisco', 'Los Angeles','New York', 'San Francisco', 'Los Angeles','New York', 'San Francisco', 'Los Angeles','New York', 'San Francisco', 'Los Angeles'],
        'number_visit' :[3, 4, 5,2, 4, 5,6, 4, 5,1, 4, 5]
        }
df = pd.DataFrame(data) # this is to just arragnge data 
plt.scatter(df.Age,df.number_visit) #this is to defined -axis and y-axis
# plt.show()  #this is to show data on graph
print(df)

def loss_function(m,b,points):
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].Age
        y=points.iloc[i].number_visit
        total_error += (y - (m * x + b )) ** 2
    total_error /  float(len(points))


def gradient_descent(m_now , b_now , points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].Age
        y = points.iloc[i].number_visit
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m= m_now - m_gradient* L
    b= b_now - b_gradient* L
    return m , b 


m =0 
b =0 
L = 0.0001
epochs = 1000


for i in range(epochs) : 
    if i % 50 == 0 :
        print(f"Epoch: {i} ")
    m ,b = gradient_descent(m , b, df , L)


print(m ,b)
plt.scatter(df.Age,df.number_visit,color="black")
plt.plot(list(range(20,50)),[m * x + b for x in range(20,50)])
plt.show()