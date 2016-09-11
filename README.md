## j3dview
View BMD/BDL files

## Requirements for the source code
# Linux
* Python 3.X (e.g. 3.4)
* PyQt4 (sudo apt-get install python3-pyqt4)
* PyOpenGL (pip3 install pyopengl, might be necessary to install pip3 first)
* PyQt4.QtOpenGL (sudo apt-get install python3-pyqt4.qtopengl)
* Numpy (sudo apt-get install python3-numpy)
* Cython (pip3 install cython)

# Windows
Requirements are the same as with Linux, but Windows has no package manager 
that would make your work easier, so you will have to look around for the required modules.

If you only want to use J3DView, a compiled release for Windows exists here: https://github.com/blank63/j3dview/releases

## How to run/install j3dview
There are two ways to do it:
* First method: You use setup.py. Read up on how to install a python program through setup.py
* Second method: You execute j3dview.py directly without using setup.py. For this, uncomment two lines about pyximport in j3dview.py


## Controls
* W, S:     Moves camera forward and backward
* A, D,     Moves camera to the left and to the right
* Q, E:     Moves camera down and up
* I, K:     Rotates camera upwards and downwards
* J, L:     Rotates camera to the left and to the right
* U, O:     Rotates camera clockwise and counter-clockwise
* Shift:    Speeds up camera movement and rotation

