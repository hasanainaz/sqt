from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Speech Quefrency Transform (SQT) - int16'
LONG_DESCRIPTION = 'Combining multiple processes, attenuating background noises, and enabling distant-speech recognition, we introduce the Speech Quefrency Transform (SQT) approach as well as multiple quefrency scales. SQT is a set of frequency transforms whose spectral leakages are controlled per a frequency-modulation model. SQT captures the stationarity of time series onto a hyperspace that resembles the cepstrogram when it is reduced for pitch track extraction. This library is an interface for Automatic Speech Recognition (ASR) for converting an audio series to and from the cepstral domain.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="SQT", 
        version=VERSION,
        author="Ahmad Hasanain",
        author_email="hasanainaz@email.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[numpy,pickle], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)