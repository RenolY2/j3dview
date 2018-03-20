# j3dview
View BMD/BDL files

# Requirements for source code 
* Python 3.4 or 3.5 (3.5 preferred)
* PyQt5 
* PyOpenGL 
* Numpy 
* Cython 

Python versions >=3.6 are affected by the following issue and will not run the code without heavy changes: https://bugs.python.org/issue29270


64 bit Windows users can find a compiled release here: https://github.com/RenolY2/j3dview/releases

# How to run/build j3dview
First, make sure you have all required dependencies installed and ``python`` needs to run one of the two python versions mentioned above.
Instead of ``python`` you could also directly type in the path to the correct python version, e.g. ``C:\Python35\python.exe``

* Running j3dview <br>
Edit j3dview.py and uncomment two lines about pyximport at the top of the file. 
Then you can run j3dview.py with python 
* Building j3dview <br>
```
python setup.py build_ext --inplace
python setup.py build
```

# Controls
* W, S:     Moves camera forward and backward
* A, D,     Moves camera to the left and to the right
* Q, E:     Moves camera down and up
* I, K:     Rotates camera upwards and downwards
* J, L:     Rotates camera to the left and to the right
* U, O:     Rotates camera clockwise and counter-clockwise
* Shift:    Speeds up camera movement and rotation

