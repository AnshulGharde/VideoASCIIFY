import cv2
import numpy as np
import os
import shutil
from Utility_Files import FrameToVideo, AsciiFrame

########################################################################################################
                                        ##START OF CODE##
        #######################################################################################
try:
    # taking input from user. Enter .mp4 or .avi file only. Because this works on that files only.
    #put the input file in the directoiry with same name.
    if(not os.path.exists("./INPUT_FILE")):
        os.makedirs("./INPUT_FILE")
        print("\"INPUT_FILE\" directory did not EXIST.")
        print("\"INPUT_FILE\" directory CREATED.")
        print("Copy the video file in this directory.")
    Vidname = input("Enter the name of video file with \".mp4\" or \".avi\" extension present in INPUT_FILE: ")

    if(not os.path.exists("./INPUT_FILE/"+Vidname)):
        print("THE FILE YOU PASSED DO NOT EXIST. CHECK AND RUN THE PROGRAM AGAIN.")
        exit()
    elif((Vidname[len(Vidname)-4:len(Vidname)]!=".mp4")and(Vidname[len(Vidname)-4:len(Vidname)]!=".avi")):
        print("THE FILE YOU PASSED IS NOT OF A EXTENTION \".mp4\" or \".avi\" extension. CHECK AND RUN THE PROGRAM AGAIN.")
        exit()
    else:
        print ("BEGINING THE CONVERSION PROCESS.")

    cam = cv2.VideoCapture("./INPUT_FILE/"+Vidname) #this reads the video file.
    out_name = Vidname[:len(Vidname)-4]
    # finding total number of frames in the video. Try to convert video with less number of frames.
    # more number of frames will take more time to get ASCIIFIED.
    total = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    print("There are in total "+ str(total) + " numbers of frame in this video.")

    # creating a new directory to save EACH asciified frame of the video.

    if(os.path.exists("./FRAMES")):
        print("Directory named \"FRAMES\" already exists. NEED TO BE DELETED and CREATED AGAIN.")
        shutil.rmtree("./FRAMES")
        print("Directory named \"FRAMES\" DELETED.")
        

    os.makedirs("./FRAMES")
    print("Directory named \"FRAMES\" is created to store asciified frames of video.")


    currentframe = 0 # variable to keep count of current frame, starting from '0'.
    i=0 # variable to use as condition in while loop given below.
    j=0 # varialble to keep count of not-compactible frames

        #######################################################################################
        #######################################################################################

    # This while loop takes every frame of the video and asciifies it.
    # after getting asciified, it is stored in the directory named \"frames\" with proper name. 
    while(i<total): #iterating the loop from i = 0 to (total -1).

        _,frame = cam.read() # reads all the frame sequentially.

        if(isinstance(frame,np.ndarray)): # we would only operate on the frame if it is in proper form of numpy.ndarray.
        
            # this is a bit hardcoded part to save the numbers of frame in a proper form of 4-digit number, as it is required afterwards.
            # "zeros" is a variable that adds right amount of zeeros to the name.
            # though I must recommend not to go beyond 1000 frames, as it takes much time to get converted and also take much space.
            if i<10:
                zeros = "000"
            elif i<100:
                zeros = "00"
            elif i<1000:
                zeros = "0"


            # making a path name where the file will be save with proper name.
            #       ./FRAMES/frame   (number of preceding zeros)        frame number         extention
            path = "./FRAMES/frame"    +        zeros      +         str(currentframe)    +   ".jpg"
            AsciiFrame.Fascii(frame,path)  # this saves the image in the directory.
            print( "Frame " + str(i) + " SCANNED and ASCIIFIED out of " + str(total)+".")

            # increasing counter so that it will show how many frames are created. Also increasing loop variable
            currentframe += 1      
            i+=1

        else:   # if frame is of insuitable format, we should skip it and increment 'j'.
                # thus stating which frame did not get compiled and increasing loop variable 
            j+=1
            print( "Frame " + str(i) + " didnt get compiled.")
            i+=1
    # since loop is ended which means we have gone through all the frames of the video.
    # thus there is no use of VideoCapture object.
    # so we will release it.
    cam.release()
    print(str(j) +" number of frames didn't get compiled.")
    
        #######################################################################################
        #######################################################################################

    # now, all the frames of the video are asciified and stored in the folder "FRAMES".
    # we just  have to combine all the images sequencial so that a video is formed.
    # below function takes care of that. Passing total number of compactible frames as a argument 
    FrameToVideo.VideoMaker((total-j),out_name)

    # returning from the above funtion, we would have the required asciified video in the directory OUTPUT_FILE with name "Project.avi".
    # thus we no longer need the frames of the videos.
    # so we will delete the directory "FRAMES" and free the disk space.
    shutil.rmtree("./FRAMES")
    print("Directory named \"FRAMES\" is deleted.")

except:
    print("EXECUTION STOPPED DUE TO SOME ERROR/EXCEPTION.")

    if(os.path.exists("./FRAMES")):
        shutil.rmtree("./FRAMES")
        print("Directory named \"FRAMES\" is deleted.")

    if(os.path.exists("./OUTPUT_FILE/"+out_name+".avi")):
        os.remove("./OUTPUT_FILE/"+out_name+".avi")


else:
    print("The Ascified video generated by the name "+out_name+".avi in OUTPUT_FILE.")

        #######################################################################################
                                            ##END OF CODE##
########################################################################################################