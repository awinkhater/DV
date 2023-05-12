#Alex Khater
#Lab 5
#Data Visualization
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#1
np.random.seed(seed=6401)
x = np.random.normal(loc=0, scale=1, size=5000 )

y=np.cumsum(x, axis=0)



plt.figure(figsize=(9,7))
for i in range (1,5):
    plt.subplot(2,2,i)
    if i==1:
        plt.plot(x)
        plt.title('Gaussian Data')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
    if i==2:
        plt.plot(y)
        plt.title('Non-Gaussian Data')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
    if i==3:
        plt.hist(x, bins=100)
        plt.title('Gaussian Data Histogram')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
    if i==4:
        plt.hist(y, bins=100)
        plt.title('Non-Gaussian Data Histogram')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()
#2
z=stats.kstest(x, "norm")
Q=stats.kstest(y, "norm")
print(f"K-S test: statistic{z[0]} p-value={z[1]}")
print(f"K-S test: x looks normal (judging by the p-value)")
print("***********************")
print(f"K-S test: statistic{Q[0]} p-value={Q[1]}")
print(f"K-S test: y looks non normal (judging by the p-value)")

#3
from scipy.stats import shapiro
z=stats.shapiro(x)
Q=stats.shapiro(y)
print(f"Shapiro test: statistic{z[0]} p-value={z[1]}")
print(f"Shapiro test: x looks normal (judging by the p-value)")
print("***********************")
print(f"Shapiro test: statistic{Q[0]} p-value={Q[1]}")
print(f"Shapiro test: y looks non normal (judging by the p-value)")

#4
x1, p1 = stats.normaltest(x)
x2, p2 = stats.normaltest(y)

print(f"da_k_squared test: statistic{x1} p-value={p1}")
print(f"da_k_squared test: x looks normal (judging by the p-value)")
print("***********************")
print(f"da_k_squared test: statistic{x2} p-value={p2}")
print(f"da_k_squared test: y looks non normal (judging by the p-value)")
#5
from scipy.stats import rankdata
from scipy.stats import norm

Y=norm.ppf(rankdata(y)/(len(y) + 1))


plt.figure(figsize=(9,7))
for i in range (1,5):
    plt.subplot(2,2,i)
    if i==1:
        plt.plot(y)
        plt.title('Non-Gaussian Data')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
    if i==2:
        plt.plot(Y)
        plt.title('Transformed Data')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
    if i==3:
        plt.hist(y, bins=100)
        plt.title('Non-Gaussian Histogram')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
    if i==4:
        plt.hist(Y, bins=100)
        plt.title('Transformed Histogram')
        plt.grid()
        plt.xlabel('# of Samples')
        plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()

#6
import statsmodels.api as sm
plt.figure(figsize=(9,7))
for i in range (1,3):
    plt.subplot(1,2,i)
    if i==1:
        stats.probplot(y, dist="norm", plot=plt)
        plt.title('Non-Gaussian Data')
        plt.grid()
        plt.xlabel('Theoretical Quantities')
        plt.ylabel('Sample Quantities')
    if i==2:
        stats.probplot(Y, dist="norm", plot=plt)
        plt.title('Transformed Data')
        plt.grid()
        plt.xlabel('Sample Quantities')
        plt.ylabel('Theoretical Quantities')
plt.tight_layout()
plt.show()

#7
z=stats.kstest(Y, "norm")
print(f"K-S test: statistic{z[0]} p-value={z[1]}")
print(f"K-S test: Transformed Data looks normal (judging by the p-value)")
#8
z=stats.shapiro(Y)
print(f"Shapiro test: statistic{z[0]} p-value={z[1]}")
print(f"Shapiro test: Transformed Data looks normal (judging by the p-value)")
#9
x1, p1 = stats.normaltest(Y)


print(f"da_k_squared test: statistic{x1} p-value={p1}")
print(f"da_k_squared test: Transformed Data looks normal (judging by the p-value)")
#10
print("Yes, All 3 tests classify the p-value as normal due to the p-value being at or near 1")
