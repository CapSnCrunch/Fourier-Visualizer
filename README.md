# Fourier-Visualizer
This project is meant to give some visual intuition on the 2-dimensional Fourier Transformation. The program allows users to draw an image while the spectrum of the image is continuously updated in another window. The opposite can be done with inverse-spectrum.py where the user draws the spectrum and the image corresponding to that drawing is displayed in another window.

Running spectrum.py and inverse-spectrum.py requires you have the cv2, numpy, and pygame libraries installed. If you don't, go to terminal and use the commands:
- pip install opencv-python
- pip install numpy
- pip install pygame

Lastly, you may need to edit the 'current-folder' and 'save-folder' variables appropriately.

Specific details on ways you can interact with the program are listed at the top of each file.

<p align='center'>
  <img src='demo imgs/demo3.JPG' width='600'>
</p>


## weave.py
Unrelated to the Fourier transform but thought I might put it in the project since it uses the same images. Lets you 'weave' two images together pixel by pixel or, by changing the block-size variable, in larger strips. Output images are fairly interesting:

<p align='center'>
  <img src='demo imgs/demo1.JPG' width='300'>
  <img src='demo imgs/demo2.JPG' width='300'>
</p>
<p style = 'text-align: center;'>
  <h1>Example of flowers + bees and flowers + city</h1>
</p>
