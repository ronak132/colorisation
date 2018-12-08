import sys
import argparse
import cv2
import os
from imageColorizer import colorkaro
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      path = 'output/'
      name = "frame"+str(count)+".jpg"	
      cv2.imwrite(os.path.join(path,name), image)     # save frame as JPEG file
      colorkaro(os.path.join(path,name))
      count = count + 1

def makeVideo():
    img=[]
    for i in range(0,5):
        img.append(cv2.imread("\\" + pathOut + str(i)+'.png'))

    height,width,layers=img[1].shape

    video=cv2.VideoWriter("/" + pathOut + '\\video.avi',-1,1,(width,height))

    for j in range(0,5):
        video.write(img)

    cv2.destroyAllWindows()
    video.release()

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
