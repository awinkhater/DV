#LMS
import matplotlib.pyplot as plt
import numpy as np
# -------------------------------------------------
p = np.array([[1, 1, 2, 2, -1, -2, -1, -2 ],
              [1, 2, -1, 0, 2, 1, -1, -2]])

t = np.array([[-1, -1, -1, -1, 1, 1, 1 , 1],
              [-1, -1, 1 ,1, -1, -1, 1, 1]])
# ----------------------------------------------


#1
plt.figure()
plt.scatter(p[0],p[1])
plt.show()
#Some points are overlapping
plt.figure()
plt.scatter(t[0],t[1])
plt.show()
#2
#Professor Jafari Approved of the preset 400 epochs.

def LMS(alpha, P,T, W, B):
    W_old=W
    W_new=W
    error=0
    a=0
    b_new=B
    b_old=B
    e=[]
    iter=[]
    #arbitrary 400 epochs
    for i in range(0, 400):
        for j in range (len(P[1])):
            p= np.array([[P[0][j]],
                         [P[1][j]]])
            t= np.array([[T[0][j]],
                         [T[1][j]]])
            a= np.add((np.matmul(W_old, p)), b_old)
            error=np.subtract(t, a)
            k=np.dot(2*alpha, error)
            q=np.transpose(p)
            Q= np.dot(k, q)
            W_new= np.add(W_old, Q)
            b_new= np.add(b_old, k)
            W_old=W_new
            b_old=b_new
            #sum square error
            E = (t[0] - a[0]) + (t[1] - a[1])
            SE = E * E
            e.append(SE)
            iter.append(i)
    return(W_new, b_old, e, iter)



def adaline(p, t):
    a = np.random.random(6)
    w1 = np.array([[a[0], a[1]],
                   [a[2], a[3]]])
    b1 = np.array([[a[4]], [a[5]]])
    x=LMS(0.001,p,t, w1, b1)
    W= x[0]
    b=x[1]
    for i in range(len (p[0])):
        I=np.array([[p[0][i]],
                    [p[1][i]]])
        O= np.dot(W, I)
        a= O + b
        print(f"point p{i+1}: a= {a}")

print(adaline(p,t))
#3
a = np.random.random(6)
w1 = np.array([[a[0], a[1]],
                   [a[2], a[3]]])
b1 = np.array([[a[4]], [a[5]]])
x=LMS(0.001,p,t, w1, b1)
W=x[0]
B=x[1]
E= x[2]
I=x[3]
plt.figure()
plt.scatter(I, E)
plt.xlabel('Epochs')
plt.ylabel('Sum Square Error')
plt.tight_layout()
plt.show()



#4
#print(W[1])
#From math we know the two decision boundaries are along the vectors ( 0.05124988, 0.59362366)
#and (0.66622595, -0.16807141)

# Creating vectors X and Y
#Equations of lines were calculated using simple algebra of the form y=mx+b
t = np.linspace(-3,3, 3)
a = 11.3728*t + B[0]
b = -0.252274*t + B[1]


plt.scatter(p[0],p[1])
plt.plot(t, a, 'r') # plotting t, a separately

plt.plot(t, b, 'b') # plotting t, b separately
plt.title("Decision Boundaries")
plt.show()

#5
#The decision boundary from the perceptron learning rule would only just barely separate the points,
#The LMS decision boundaries would move as far from the prototype patterns as possible to ensure
#a more general and applicable classification rule.