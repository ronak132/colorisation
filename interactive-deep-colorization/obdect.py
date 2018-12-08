import sys
import argparse
import cv2
import os
#from imageColorizer import colorkaro
print(cv2.__version__)
from yolo import getObject

FPS = 25
def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000/FPS))    # added this line
        success,image = vidcap.read()
        if success:
            print ('Read a new frame: ', success)
            #path = 'output/'
            name = "frame"+str(count)+".jpg"
            #cv2.imwrite(os.path.join(path,name), image)     # save frame as JPEG file
            print(name)
            cv2.imwrite(name,image)
            #colorkaro(name)
            x,y = getObject(name)
            if (x and y):
                os.system("python inputColorize.py -img_in " + name +" -img_out " + "out-" + name + " -a 40 -b 62 -height "+str(x)+" -width "+str(y))
            else:
                os.system("python inputColorize.py -img_in " + name +" -img_out " + "out-" + name + " -a 40 -b 62 -height "+str(10)+" -width "+str(10))
            #os.system("python colorize.py -img_in " + name +" -img_out " + "out-" + name)
            #os.system("python inputColorize.py -img_in " + name +" -img_out " + "out-" + name + " -a -93 -b 101 -height "+str(x)+" -width "+str(y))
            count = count + 1
    return count-2

def makeVideo(count):
    img=[]
    for i in range(0,count):
        img.append(cv2.imread('out-frame'+str(i)+'.jpg'))

    height,width,layers=img[1].shape

    #video=cv2.VideoWriter('video.avi',-1,1,(width,height))
    video = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*"MJPG"), FPS,(1280,1280))

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