import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

########################################################################################################
                                        ##START OF CODE##
        #######################################################################################

# this function plays a important role.
# the image is stored in numpy.ndarray as BGR
# this means index 0 ==> BLUE, 1==> GREEN, 2 ==> RED.
# but while saving the image, we are saving it as RGB.
# thus we need to swap R and B component of the image before asciifing it so that its true color are shown in the asciifed form.
def invert_BGR_to_RGB(image):
    len, bre , dim = image.shape
    for x in range(len):
        for y in range(bre):
            temp = image[x][y][0]
            image[x][y][0] = image[x][y][2]
            image[x][y][2] = temp
    
    return image

        #######################################################################################
        #######################################################################################

def Fascii(image,path):

    # BackGround color is set to (75, 75, 75) since i dont want it to be completely black.
    # because when a light color is to be denoted with low luminosity(wrt black BackGroung),
    # the black color dominate the pixel.   
    bg_code = (75, 75, 75)

    #still if you want a black BackGround set it as giveb below.
    #bg_code = (0, 0, 0)

    # Characters used for Mapping to Pixels
    char_list = "$@B%8&WM#HK*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?_+=-~<>i!lI;:,\"^`'. "

    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 1.55
    
    #swaping R and B component
    image = invert_BGR_to_RGB(image)

            ##############################################################################
            ##############################################################################

    
    num_char = len(char_list)
    num_cols = 300 # this defines how many number of columns are there in asciified picture 

    height, width, _ = image.shape

    cell_w = width/num_cols         # these are simple
    cell_h = scale * cell_w         # mathematical calculations
    num_rows = int(height/cell_h)   # for pixel dimension

    char_width, char_height =font.getsize("A")  # these are simple
    out_width = char_width * num_cols           # mathematical calculations
    out_height = char_height * num_rows         # for output image dimension

    out_image = Image.new("RGB",(out_width, out_height), bg_code)

    # creating an instance of Draw class.
    draw = ImageDraw.Draw(out_image)

            ##############################################################################
            ##############################################################################

    # mapping Characters for RGB

    for i in range(num_rows):
        for j in range(num_cols):
            partial_image = image[int(i*cell_h):min(int((i + 1)*cell_h), height),
                            int(j*cell_w):min(int((j+1)*cell_w), width),:]
        
            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cell_h*cell_w)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())

            c = char_list[min(int(np.mean(partial_image)*num_char/255), num_char - 1)]
            draw.text((j*char_width,i*char_height), c, fill=partial_avg_color, font = font)

            ##############################################################################
            ##############################################################################

    # inverting Image and removing excess borders
    cropped_image = out_image.getbbox()

    # saving the new Image
    out_image = out_image.crop(cropped_image)
    out_image.save(path)

        #######################################################################################
                                            ##END OF CODE##
########################################################################################################