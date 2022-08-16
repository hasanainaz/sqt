# Speech Quefrency Transform (SQT)

This is an Automatic Speech Recognition (ASR) interface that converts speech audio to and from the cepstral domain. In other words, it extracts the locally stationary speech featuers from the speech signals, and it reconstructs them back to speech singals. It represents the speech series by two features and has several applications. 

### Jupyter Notebook Demo
1. [Browse the static HTML demo](https://htmlpreview.github.io/?https://github.com/hasanainaz/sqt/blob/master/docs/demo.html)
2. Or: [Run the Jupyter Notebook live in Google CoLab](https://colab.research.google.com/github/hasanainaz/sqt/blob/master/docs/demo.ipynb) 


### Repository 
For Developers: [github.com/hasanainaz/sqt](https://github.com/hasanainaz/sqt)

### Citation 
For Researchers: [Hasanain, A., Syed, M., Kepuska, V., Silaghi, M. (2022). Multi-Dimensional Spectral Process for Cepstral Feature
Engineering & Formant Coding. J Electrical Electron Eng, 1(1), 01-20.](https://opastpublishers.com/open-access/multi-dimensional-spectral-process-for-cepstral-feature-engineering-rnformant-coding.pdf)


### Abstract 
The efficient use of a communication bandwidth starts with the data source. The features of the speech signals can be extracted and reconstructed to lower the Internet traffic of the acoustic artificial agents and increase the quality of the automatic speech recognition systems. The Speech Quefrency Transform (SQT) is hereby introduced in the work to enrich the communication space between the artificial agents and mankind. We describe the motivation, methodology, and deep learning approach in detail as we apply the SQT technology to several applications: sharp pitch track extraction, real-time speech communications, and emotion recognition. Combining multiple processes, attenuating background noises, and enabling distant-speech recognition, we introduce the SQT cepstrograms as well as multiple quefrency scales. SQT is a set of frequency transforms whose spectral leakages are controlled per a frequency-modulation model. SQT captures the stationarity of time series onto a hyperspace that resembles the cepstrogram when it is reduced for pitch track extraction. This library is an interface for Automatic Speech Recognition (ASR) for converting an audio series to and from the cepstral domain. 


#### Speech Featrues
1. Pitch Tracks
2. Responsive-Band Spectrograms (harmonic series). 
    
#### Quefrency Scales
1. Linear-Space
2. Reciprocal (this is similar to the MFCC scale)
3. Geometrical (this is based on the two dimensional view of the pitch function)

#### Applications
1. Speech Analysis and Synthesis 
2. Natural Language Processing (NLP)
3. Machine Learning (ML)
4. Telecommunications



# Python Library

To get started, please the following instructions. There is also a Jupyter Notebook Demo in the package directory. 

1. Install:
```
pip install sqtpy
```

2. Initalize a new instance
```
import sqtpy
sqt = sqtpy.SQT( N = 50 , Rs = 30 , Fs = 8000 )
```

3. Extract Pitch Track and speech features
```
[F0, Hm, Et] = sqt.encode( I0 )
```

4. Estimate the original speech signal from the extracted speech features
```
I = sqt.decode( F0, Hm )
```

### The Int16 Class

We prepared this version of the sqt library for the Raspberry Pi combatablity. This version prioritizes space over speed and quality. In this vesrion, 256-level variables are multiplied while they are in 16-bit-integer-data type, and its temporal and cepstral filterings are done sequantally inside for-loops, so low-order filtering is sticktly recommened in this version. 
```
sqt = sqtpy.SQTint16( N = 50 , Rs = 30 , Fs = 8000 )
```

# JavaScript Library

No JS version has been released yet. [Please check again later](https://www.ahmadzuhair.com/sqt_qualitycheck/). 






# License: 

The SQT programs are free software. They are provided for personal use in the hope that they will be useful but without any warranties, including without limitation warranties of fitness for a particular purpose and merchantability. For commerical, please find the open-source license. 
```
GNU Affero General Public License v3
```


AhmadZuhair.com © 2022
