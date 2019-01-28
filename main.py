import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GMM
from sklearn.mixture import GaussianMixture
from scipy.spatial.distance import cdist
import requests

import MFCCopt as mfcc
import pyaudioRecord
import eliminateNoise

num=20
X=mfcc.makeMFCC("brittoOven",num)
Y=mfcc.makeMFCC("brittoKettle",num)
X=X+Y
gmm = GaussianMixture(n_components=2, covariance_type='full', random_state=0).fit(X)
labels=gmm.predict(X)
labels=list(labels)

while 1:
    inp=int(input("Enter"))
    Test6_pyaudio.recordSample()
    Test10_eliminate.reduceNoise()
    Z=mfcc.makeMFCC("file",1)
    Z=gmm.predict(Z)    
    if(inp==0):
        p=requests.get('http://192.168.43.171:8000/realTime/tellResponse/?=userAnswer:1,')
        print("Britto said Oven")
    else:
        p=requests.get('http://192.168.43.171:8000/realTime/tellResponse/?=userAnswer:0,')
        print("Britto said Kettle")
