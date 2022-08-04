# Speech Quefrency Transform

## Python

### The Int16 Version

1. Install:
```
pip install -i https://test.pypi.org/simple/ sqtpy==0.0.2
```

2. Initalize a new instance
```
import sqtpy
sqt = sqtpy.SQT( N = 500 , Rs = 300 , Fs = 8000 )
```

3. Extract Pitch Track and speech features
```
[F0, Hm, Et] = sqt.encode( I0 )
```

4. Estimate the original speech signal from the extracted speech features
```
I = sqt.decode( F0, Hm )
```

Note: there is a Jupyter Notebook demo in the package directory. 
