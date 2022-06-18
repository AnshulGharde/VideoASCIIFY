import cv2
import numpy as np
import glob
import os

########################################################################################################
                                        ##START OF CODE##
        #######################################################################################

def VideoMaker(total,out_name,fps:int):

    img_list = [] #creating a empty list to store all the frames.
    count=0 #variable to keep count of current frame, starting from '0'.

    # this for loop iterates over all the files present in the "FRAMES" directory, with extention .jpg
    # it will traverse in increing order
    # thus we saved all the frame number in 4-digit number  
    for filename in glob.glob("./FRAMES/*.jpg"):
        img = cv2.imread(filename) # reads image file as a numpy.ndarray from the path provided
        print( "Frame " + str(count) + " COPIED.")
        img_list.append(img) # appends the image(<class 'numpy.ndarray'>) to the list
        count+=1 # incrementing count
    # when the loops ends, all the frames are stored in the list.
    
        #######################################################################################
        #######################################################################################

    # here, to set the dimensions of the video, we will take first frame of the video.
    img = cv2.imread("./FRAMES/frame0000.jpg")
    height, width, layers = img.shape
    size = (width,height)

    # making an object of VideoWriter class, to compile video, with the given constructor parameters
    if(not os.path.exists("./OUTPUT_FILE")):
        os.makedirs("./OUTPUT_FILE")

    out = cv2.VideoWriter("./OUTPUT_FILE/"+out_name+".avi",cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    # this will store the video in the same directory under the name "Project.avi".
    # fps is the frames per second, taken from the video itself.
    # size specifies the dimensions of the video.
    
        #######################################################################################
        #######################################################################################
    
    # this for loop takes one frame for the list and writes it to the video.
    for i in range(len(img_list)):
        out.write(img_list[i])
        print( "Frame " + str(i) + " ADDED to video out of " + str(total))

    # getting out of the loop means we have completed the video making process.
    # thus we release the instance of VideoWriter class.
    out.release()

        #######################################################################################
                                            ##END OF CODE##
########################################################################################################
