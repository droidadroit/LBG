# Image compression using LBG
A lenna image is compressed by vector quantization using Linde-Buzo-Gray algorithm. The image is divided into blocks of base size (say `4 x 4`) and the corresponding vectors are fed to the LBG algorithm. This generates a codebook of a predetermined size which is used to generate the reconstructed image.  
## Getting Started
### Prerequisites
1. **Anaconda for Python 2.7**
2. **OpenCV for Python 2.7**  
### Installing
1. **Anaconda for Python 2.7**  
Go to the [downloads page of Anaconda](https://www.anaconda.com/download/) and select the installer for Python 2.7. Once downloaded, installing it should be a straightforward process. Anaconda has along with it most of the packages we need.   

2. **OpenCV for Python 2.7**  
This [page](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html) explains it quite well.  
## Running
Before running `lbg_random.py` for randomly initialized codebook and `lbg_split.py` for codebook initialized by splitting technique, there are a few parameters to be set.  
```python
image_location
bits_per_codevector
block_width
block_height
```  
`image_location` is set to the relative location of the image from the current directory.  
`bits_per_codevector` is set based on the size of the codebook you desire. For e.g., for a 256-vector codebook, this value should be `8` as `2^8 = 256`.  
`block_width` and `block_height` are set to the size of the blocks the image is divided into. Make sure the blocks cover the the entire image.  
`perturbation_vector` in `lbg_split.py` can be changed manually.  

Once the parameters are set, enter the following command to run the script.  
`python [name of the script] [image_location] [bits_per_codevector] [block_width] [block_height]`

**Please read the [wiki](https://github.com/droidadroit/LBG/wiki/LBG) for an understanding of the above terms.**  
## Results
For the image compressed using `lbg_random.py`, click [here](https://github.com/droidadroit/LBG/tree/master/Results/lbg_random).  
For the image compressed using `lbg_split.py`, click [here](https://github.com/droidadroit/LBG/tree/master/Results/lbg_split).  

The following are the parameters used.  
```python
block_width = 4
block_height = 4
```
`bits_per_codevector` ranged from `1` to `10`.


