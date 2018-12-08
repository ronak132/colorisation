from data import colorize_image as CI
import matplotlib.pyplot as plt
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='iColor: deep interactive colorization')
    parser.add_argument('-img_in',dest='img_in',help='grayscale image to read in', type=str)
    parser.add_argument('-img_out',dest='img_out',help='colorized image to save off', type=str)
    parser.add_argument('-a',dest='a',help='input point a value', type=int)
    parser.add_argument('-b',dest='b',help='input point b value', type=int)
    parser.add_argument('-height',dest='h',help='input point h value', type=int)
    parser.add_argument('-width',dest='w',help='input point w value', type=int)

    args = parser.parse_args()
    return args

def put_point(input_ab,mask,loc,p,val):
    # input_ab    2x256x256    current user ab input (will be updated)s
    # mask        1x256x256    binary mask of current user input (will be updated)
    # loc         2 tuple      (h,w) of where to put the user input
    # p           scalar       half-patch size
    # val         2 tuple      (a,b) value of user input
    input_ab[:,loc[0]-p:loc[0]+p+1,loc[1]-p:loc[1]+p+1] = np.array(val)[:,np.newaxis,np.newaxis]
    mask[:,loc[0]-p:loc[0]+p+1,loc[1]-p:loc[1]+p+1] = 1
    return (input_ab,mask)

#%matplotlib inline

args = parse_args()

# Choose gpu to run the model on
gpu_id = 0

# Initialize colorization class
colorModel = CI.ColorizeImageCaffe(Xd=256)

# Load the model
colorModel.prep_net(gpu_id,'./models/reference_model/deploy_nodist.prototxt','./models/reference_model/model.caffemodel')
#colorModel.load_image('./imgs/rose.jpeg') # load an image #todo remove hardcoding
colorModel.load_image(args.img_in) # load an image #todo remove hardcoding
mask = np.zeros((1,256,256)) # giving no user points, so mask is all 0's
input_ab = np.zeros((2,256,256)) # ab values of user points, default to 0 for no input #todo remove hardcoding
img_out = colorModel.net_forward(input_ab,mask) # run model, returns 256x256 image

#img_gray_fullres = colorModel.get_img_gray_fullres() # get grayscale image at fullresolution
#img_out_fullres = colorModel.get_img_fullres() # get image at full resolution

# add a blue point in the middle of the image
#(input_ab,mask) = put_point(input_ab,mask,[135,160],3,[-23,69])
(input_ab,mask) = put_point(input_ab,mask,[args.h,args.w],3,[args.a,args.b])

# call forward
img_out = colorModel.net_forward(input_ab,mask)

# get mask, input image, and result in full resolution
img_out_fullres = colorModel.get_img_fullres() # get image at full resolution

# show user input, along with output
plt.figure(figsize=(10,6))

plt.imsave(args.img_out, img_out_fullres)

