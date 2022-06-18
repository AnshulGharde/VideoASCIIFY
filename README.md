# VideoASCIIFY-ER
This code will let you ASCIIFY video file(.mp4 and .avi are preferred)

It is written in python programming language.
So, it’s necessary that python code works on your machine.
I have used the python libraries, so it’s required that you instal them too
1)OpenCV
	a. pip install opencv-python
	b. pip install opencv-python-headless
2)pillow 
	a. pip install pillow
(If the import in the code gives error, try to give correct path according to your computer. Or copy the cv2, numpy and PIL directory in this folder where you extract my code)

**HOW TO RUN:**

All you need is to run the VideoASCIIFY.py file.
Copy the input video file in the INPUT_FILE.
After running the VideoASCIIFY.py file, it will ask for name of the video file.
Enter video file name with proper extension of .mp4 or. avi. (Other format might give poor result)

If you give these all input correctly, the output video will be stored in the directory OUTPUT_FILE with the same name and extension .avi.

**THE INTERNAL WORKING:**

As we know, a video file is collection of images only.
The code will take the video file and extract each frame.
Each frame is ASCII-fied with the help of AsciiFrame.py present in Utility_Files.
It uses opencv and pillow library to collect image data in numpy.ndarray form of GRB color scheme.

Once each frame is ASCII-fied, the video is compiled with the help of FrameToVideo.py present in Utility_Files.
This goes through all the frames and makes a list of the image data, and then added to video file.
The ASCII-fied video will be stored in the directory named OUTPUT_FILE with the same name as input file and extension will be .avi.

**For detailed explanation of WORKING of the code, go through the code itself as I have commented the details of code.**

**SOME THINGS TO KNOW BEFORE RUNNIG THE CODE:**
1) The ASCII-fication takes more time if number of frames are more(obviously) and resolution each frame.
Also, the video generated will take considerable amount of space on disk.
This depends on the variable num_cols on the line51 of Utility_Files /AsciiFrame.py. currently it is set to 300.
If you wish you can go and change it there. Refer to the frame examples and its size in the folder FrameExamples/column

2) The output video is compiled at 24 frames per second (FPS) as set at line 37 of Utility_Files /FrameToVideo.py.
If you want, you can go and change the FPS there.
For more information go to 
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video section SAVING A VIDEO

3) the background color is set to (75, 75, 75) but you can set it to black(0, 0, 0) or white (255, 255, 255) as you wish.
see the difference in the FrameExamples/BackGround
        
**MY LEARNINGS AND TAKEAWAYS:**
While working on this project,
1) I learned how to manipulate image data using opencv, pillow and python.
2) I learned how to make and delete directory using os and shutil in-built library.
3) Handling different types errors and exceptions.
