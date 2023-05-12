import plotly.express as px
import pandas as pd
import numpy as np
from numpy import linalg as LA
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import cv2
#DASH
#(He claims its easy)




#===================
# IMAGE PCA
# img= cv2.imread('dog.jpg')
# plt.imshow(img)
# plt.show()
#
# pca= PCA(50)
#
# blue, green, red= cv2.split(img)
#
# red_transformed = pca.fit_transform(red)
# red_inverted = pca.inverse_transform(red_transformed)
#
# green_transformed = pca.fit_transform(green)
# green_inverted = pca.inverse_transform(green_transformed)
#
# blue_transformed = pca.fit_transform(blue)
# blue_inverted = pca.inverse_transform(blue_transformed)
#
# img_compressed= (np.dstack((red_inverted, green_inverted, blue_inverted))).astype(np.uint8)
# plt.imshow(img_compressed)
# plt.show()

# #SEE HIS CODE ^^^ YOU missed some


# np.random.seed(123)
# x1= np.random.normal(0,1,1000)
# x2= np.random.normal(0,1,1000)
# x3= np.random.normal(0,1,1000)
# x4= np.random.normal(0,1,1000)
#
# X= np.vstack((x1,x2,x3,x4)).T

#===================================
# #SVD ANALYSiS
# _,s,_= np.linalg.svd(X)
# print(f'svd values : {s}')
#Values not near 0 are good
#===================
# #Colinearity check bad if over 100. Really bad if over 1000
# print(LA.cond(X))
#===================
#PCA
#Need Dummy and One hot Encoder To deal with categorical
# iris= px.data.iris()
# feature= iris.columns[:-2]
# X=iris[feature].values
# Y=iris['species'].values
# pca=PCA(n_components='mle', svd_solver='full')
# pca.fit(X)
#
# plt.plot(np.cumsum(pca.explained_variance_ratio_)*100)
#
# plt.grid()
# plt.show()
