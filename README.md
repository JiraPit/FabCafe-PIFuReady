# PIFu-READY [2D-to-3D Human Digitization]
An upgraded, compact, and ready-to-run version of PIFuHD suitable for Windows and MacOS devices with only CPU

This repository contains a pytorch implementation of "Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization".

![alt text](https://camo.githubusercontent.com/dcfd98e18f6313ca98a2388a026706ffb90ff9caa383a5e487b778028376dae8/68747470733a2f2f7368756e73756b65736169746f2e6769746875622e696f2f5049467548442f7265736f75726365732f696d616765732f7069667568642e676966)

visit the original researches:

&ensp;&ensp;Facebook: https://github.com/facebookresearch/pifuhd
  
&ensp;&ensp;Shunsuke Saito: https://github.com/shunsukesaito/PIFu
# Set up
1. Open Command Prompt 

&ensp;&ensp;notes: GIT, bash, and python3 are required; if not installed, visit

&ensp;&ensp;&ensp;&ensp; GIT: https://git-scm.com/downloads

&ensp;&ensp;&ensp;&ensp; Python: https://www.python.org/downloads/

2. Clone this repository and ```cd``` into it
```
git clone https://github.com/JiraPit/PIFu-READY.git
```
```
cd PIFu-Ready
```
3. Run setup.py 

This will automatically install all python libraries required, download essential pre-trained models, and install Openpose from https://github.com/CMU-Perceptual-Computing-Lab/openpose
```
python setup.py
```
This may take a while (up to hours).

# Run
1. Store your images in a single folder (The folder can be named arbitrarily but may not contain space)
2. Simply run the following command (Replace {YOUR_IMAGES_DIRECTORY} with your folder name, also delete the {} symbol).
```
python run.py --input {YOUR_IMAGES_DIRECTORY}
```
After that, an OBJ 3d model will be created in the ```{YOUR_IMAGES_DIRECTORY}/pifuhd_final/recon``` folder.

JIRA PITAKWONG
