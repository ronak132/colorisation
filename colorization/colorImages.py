import sys
import argparse
import cv2
import os
from imageColorizer import colorkaro
print(cv2.__version__)

#FPS = 25

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    for root, dirs, files in os.walk('inputs/'):
        for fname in files:
            inpath = os.path.join('inputs/',fname)
            print(inpath)
            outpath = os.path.join('outputs/',fname)
            print(outpath)
            os.system("python colorize.py -img_in " + inpath +" -img_out " + outpath)
    return 

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    count = extractImages(args.pathIn, args.pathOut)
   #makeVideo(count)
