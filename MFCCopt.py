import python_speech_features 
from python_speech_features import mfcc
from python_speech_features import logfbank
from python_speech_features import ssc
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

def makeMFCC(name,sampleSize):
    rate=[[]for i in range(sampleSize)]
    sig=[[]for i in range(sampleSize)]
    mfcc_feat=[[]for i in range(sampleSize)]
    fbank_feat=[[]for i in range(sampleSize)]
    for i in range(sampleSize):
        wordIs=name
        word=wordIs+str(i)+".wav"
        (rate[i],sig[i])=wav.read(word)
        mfcc_featI=mfcc(sig[i],rate[i],nfft=1103)
        fbank_featI=logfbank(sig[i],rate[i],nfft=1103)
        ssc_featI=ssc(sig[i],rate[i],nfft=1103)
        for j in ssc_featI:
            fbank_feat[i].append(np.average(j))
    plt.figure()
    plt.plot(fbank_feat)
    plt.savefig("Result/MFCCaverage.png", dpi =300)
    return fbank_feat

def makeMFCCOne(name,sampleSize):
    fbank_feat=[]
    wordIs=name
    word=wordIs+str(sampleSize)+".wav"
    (rates,sigs)=wav.read(word)
    mfcc_featI=mfcc(sigs,rates)
    fbank_featI=logfbank(sigs,rates)
    for j in mfcc_featI:
        fbank_feat.append(np.average(j))
    return fbank_feat