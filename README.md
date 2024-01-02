# PIFuR - 3D Human Digitization
An upgraded, compact, and ready-to-run version of PIFu suitable for Windows and MacOS devices with only CPU.

This repository contains a pytorch implementation of "Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization".

visit the original research:

&ensp;&ensp;Shunsuke Saito: https://github.com/shunsukesaito/PIFu
# Set up
1. Open Command Prompt 

&ensp;&ensp;GIT, bash, and python3 are required; if not installed, visit

&ensp;&ensp;&ensp;&ensp; GIT: https://git-scm.com/downloads

&ensp;&ensp;&ensp;&ensp; Python: https://www.python.org/downloads/

2. Clone this repository and ```cd``` into it
```
git clone https://github.com/JiraPit/PIFuR-3DHumanDigitization.git
```
```
cd PIFuR-3DHumanDigitization
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
