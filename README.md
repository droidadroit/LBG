# Image compression using LBG
A lenna image is compressed using Linde-Buzo-Gray algorithm for vector quantization. The image is divided into blocks of size *4 x 4* and the corresponding vectors are fed to the LBG algorithm. This generates a codebook of a predetermined size which is used to generate the reconstructed image. 
## Getting Started
### Prerequisites
```
Anaconda for Python 2.7
```
```
OpenCV for Python 2.7
```
### Installing
```
Anaconda for Python 2.7
```
Go to the [downloads page of Anaconda](https://www.anaconda.com/download/) and select the installer for Python 2.7. Once downloaded, installing it should be a straightforward process. Anaconda has along with it most of the packages we need.
```
OpenCV for Python 2.7
```
This [page](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html) explains it quite well.
## Running
Run [lbg_random.py](https://github.com/droidadroit/LBG/blob/master/lbg_random.py) for randomly initialized codebook. Run [lbg_split.py](https://github.com/droidadroit/LBG/blob/master/lbg_split.py) for codebook initialized by splitting technique.  
There are a few parameters to be set before running the code.
```python
bits_per_codevector
```
Set this based on the size of the codebook you desire. For e.g., for a 256-vector codebook, this value should be 8 as 2^8=256.  
```python
block_width
block_height
```
Set this to the size of the blocks you want the image to be divided into. Make sure the blocks cover the the entire image.
```
perturbation_vector
```
This is to be set only for `lbg_split.py`.  

**Please read the [wiki](https://github.com/droidadroit/LBG/wiki/LBG) for an understanding of the above terms.**


