# Auto-colorisation
CSCE 636: Neural Networks
Let there be color : Automatic colorisation of grayscale images and videos

Contributors:
=========================
- Ronak Chaudhary <br>
- Christopher Jacob M <br>

Environment Dependencies for train and test:
=========================
- Python 3.6 <br>
- caffe-gpu <br>

Library Dependencies for running code of colorising images and videos:
=====================
- matplotlib <br>
- numpy <br>
- sys <br>
- glob <br>
- pillow <br>
- h5py <br>

## Usage

After the requirements have been installed, following things can be done:<br>

A) For colorisating without input, go to colorisation directory and run the following commands as per use:<br>
  1) For coloring a gray-scale image<br>
    `python colorize.py -img_in rose.jpeg -img_out rose_out.jpeg`<br>
  2) For coloring multiple photos, put them in inputs directory. Run the folowing command and the colorised photos will be put in outputs directory:<br>
     `python colorImages.py --pathIn inputs/ --pathOut outputs/`<br>
  3) For coloring a video, go to the colorisation directory <br>
    `python videoColorizer.py --pathIn dog.mp4 --pathOut ""`<br>  
    
    
B) For coloring with input, go to interactive-deep-colorization directory and run the following commands as per use:<br>
   1) For coloring a gray-scale image with input points x and y and (a,b) as color poings in CIELAB color space <br>
    `python inputColorize.py -img_in dog.jpg -img_out dog_out.jpg -a a -b b -height x -width y`<br>
    e.g. for point (x,y) = (50,50) and (a,b) = (40,62), the command is <br>
    `python inputColorize.py -img_in dog.jpg -img_out dog_out.jpg -a 40 -b 62 -height 50 -width 50`<br>
   2) For coloring a video with object detection, <br>
    `python obdect.py --pathIn dog_bw.mp4 --pathOut ""`
  

Git references:
---------------
- https://github.com/richzhang/colorization

## References 

[1] Zhang, Richard and Isola, Phillip and Efros, Alexei A. [Colorful Image Colorisation](https://arxiv.org/pdf/1603.08511.pdf)<br>
[2] Zhang, Richard and Zhu, Jun-Yan and Isola, Phillip and Geng, Xinyang and Lin, Angela S and Yu, Tianhe and Efros, Alexei A. [Real-Time User-Guided Image Colorization with Learned Deep Priors](https://arxiv.org/abs/1705.02999)

