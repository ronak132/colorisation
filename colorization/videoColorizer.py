import sys
import argparse
import cv2
import os
from imageColorizer import colorkaro
print(cv2.__version__)

FPS = 25

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000/FPS))    # added this line 
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      #path = 'output/'
      name = "frame"+str(count)+".jpg"	
      #cv2.imwrite(os.path.join(path,name), image)     # save frame as JPEG file
      cv2.imwrite(name,image)
      #colorkaro(name)
      os.system("python colorize.py -img_in " + name +" -img_out " + "out-" + name)
      count = count + 1
    return count-2

def makeVideo(count):
    img=[]
    for i in range(0,count):
        img.append(cv2.imread('out-frame'+str(i)+'.jpg'))

    height,width,layers=img[1].shape

    #video=cv2.VideoWriter('video.avi',-1,1,(width,height))
    video = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*"MJPG"), FPS,(640,480))

    for j in range(0,count):
        video.write(img[j])

    #cv2.destroyAllWindows()
    video.release()

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    count = extractImages(args.pathIn, args.pathOut)
    makeVideo(count)
