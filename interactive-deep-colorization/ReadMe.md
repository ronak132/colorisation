For coloring with input, run the following commands as per use:<br>
   1) For coloring a gray-scale image with input points x and y and (a,b) as color poings in CIELAB color space <br>
    `python inputColorize.py -img_in dog.jpg -img_out dog_out.jpg -a a -b b -height x -width y`<br>
    e.g. for point (x,y) = (50,50) and (a,b) = (40,62), the command is <br>
    `python inputColorize.py -img_in dog.jpg -img_out dog_out.jpg -a 40 -b 62 -height 50 -width 50`<br>
   2) For coloring a video with object detection, <br>
    `python obdect.py --pathIn dog_bw.mp4 --pathOut ""`
    
   ![dog with just colorisation](dog_color.JPG?raw=true "Title")<br>
   ![dog with red input](dog_color1.png?raw=true "Title")<br>
   ![dog with green input](dog_color2.JPG?raw=true "Title")<br>
   
   Coloring dog with custom colors<br>
   
   
   
   ![rose with just colorisation](rose_vanila.png?raw=true "Title")<br>
   ![rose with red input](rose_input1.png?raw=true "Title")<br>
   ![rose with green input](rose_input2.png?raw=true "Title")<br>
   
   Coloring rose with custom colors
