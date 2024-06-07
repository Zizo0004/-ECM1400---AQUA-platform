

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, util #COULD NOT INSTALL THIS LIBRARY ON VS CODE DUE TO PYTHON 3.11 ERROR. Code was completed on jupiter notebook and transferred to vs code





def find_red_pixels(map_filename, upper_threshold =100,lower_threshold = 50):
    """ Gets the map image file path as an input and return a binary image of the map with the red colored pixels segmented 

    Parameters:
    
    map_filename: str
        Path of the map image
    upper_threshold: int = 100
        The upper allowable threshold for the color segmentation (default is 100)
    lower_threshold: int = 50
        The lower allowable threshold for the color segmentation (default is 50)

    Returns:
    
    np.array
        A 2-dimenional np array representing the binary image of the red segmented color

    """
    #image being read with imread function
    original_img = plt.imread(map_filename)
    #height and width assigned
    height, width, _ = original_img.shape
     
    #creating numpy array
    red_binary = np.zeros((height, width))
    
    for row in range(0,height):
        for col in range(0, width):
            r = int(original_img[row,col][0]*255)
            g = int(original_img[row,col][1]*255)
            b = int(original_img[row,col][2]*255)
            #if statement to check for red colored pixel
            if r > upper_threshold and g < lower_threshold and b < lower_threshold:
                red_binary[row,col] = 255
    red_binary = red_binary.astype(np.uint8)
    #save image file to map-red-pixels.jpg
    io.imsave('map-red-pixels.jpg', red_binary, check_contrast=False)
    #displays map-red-pixels.jpg
    io.imshow(red_binary); io.show()
    #returns 2d array
    return red_binary


#* TASK MI-1b ====================================

def find_cyan_pixels(map_filename, upper_threshold = 100, lower_threshold =50):
    """ Gets the map image file path as an input and return a binary image of the map with cyan color pixels segmented

    Parameters:
    
    map_filename: str
        Path of the map image
    upper_threshold: int = 100
        The upper allowable threshold for the color segmentation default is 100
    lower_threshold: int = 50
        The lower allowable threshold for the color segmentation default is 50

    Returns:
    
    returns np.array
        A 2-dimenional np array representing the binary image of the cyan segmented color
    
    """
    #reads map using imread function
    original_img = plt.imread(map_filename)
    #height width assigned
    height, width, _ = original_img.shape

    #creates np array
    cyan_binary = np.zeros((height, width))
    
    for row in range(0,height):
        for col in range(0, width):
            r = int(original_img[row,col][0]*255)
            g = int(original_img[row,col][1]*255)
            b = int(original_img[row,col][2]*255)
            # if statment, used to check cyan color pixel
            if r < lower_threshold and g > upper_threshold and b > upper_threshold:
                cyan_binary[row,col] = 255
    
    cyan_binary = cyan_binary.astype(np.uint8)
    #saves output to map-cyan-pixels.jpg
    io.imsave('map-cyan-pixels.jpg', cyan_binary, check_contrast=False)
    #shows image
    io.imshow(cyan_binary); io.show()
    #returns 2d array
    return cyan_binary
        

def find8Neighbours(q_mn: dict): 
    """ It is a supporting function that calculates the 8 adjecent neighbors of a pixel
        not a part of function template
    
    Parameters:
    
    q_mn:
        A dictionary which contains x and y coordinates of the pixel of which the neighbors are to be found
    Returns:
    
    np.array
        an array containing the x and y coordinates of the 8 adjecent neighbors of the input pixel
    
    """
    #empty list to append
    neighbors = []

    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == 0 and dy == 0: continue # skipping the coordinates of q_mn as it is already known
            # calculating the coordinates of 8 neighbors
            neighbor_cord_x = int(q_mn['x_cord'] + dx)
            neighbor_cord_y = int(q_mn['y_cord'] + dy)
            neighbors.append([neighbor_cord_x, neighbor_cord_y])

    return neighbors




def detect_connected_components(IMG):
    """ This function is used to find the connected components from a binary image saved from Task-1(a). 
    
    Takes the binary image and returns an array which the  pixels are marked as either visited or in-visited (1, 0 respectively)
    also outputs the connected components information to a txt file named cc-output-2a.txt

    Parameters:
    
    IMG: np.array
        A binary image (obtained from the task M1)
    Returns:
    
    np.array
        An array of same size as input image which marks the visited and unvisited pixels from the input image
    
    """
    
    rows, col = IMG.shape
    #Step 1: set MARK as unvisited
    MARK = np.zeros((rows,col))     
    #Step 2: Empty queue-like array
    Q = []  
    
    # connected components counter
    connected_component_qty = 0
    # the index of this array will tell the Sr of connected component
    pixels_qty_in_component_list = []    
    
    for x in range(rows-1):
        for y in range(col-1):
            px = IMG[x, y]  #Step 3: for each pixel in image
            # if px > 0: print(px)
            if px == 1 and MARK[x, y] == 0: # if p(x,y) is pavement pixel and MARK(x,y) is unvisited
                MARK[x,y] = 1   # Set MARK(x,y) as visited
                
                connected_component_qty += 1
                
                # saving x and y coordinates of the q(m,n) pixel to calculate the 8 neighbors
                px_cord = {'x_cord': x, 'y_cord': y}

                Q.append(px_cord)    #adding p(x,y) in the Q
                pixels_qty = 1
                while len(Q)>0:     #while Q is not empty
                    q_mn = Q[0]
                    Q.remove(q_mn)      #removing 1st element from the Q

                    eight_neighbors = find8Neighbours(q_mn)

                    for neighbor in eight_neighbors:        #* for each 8-neighbor  n(s,t) of q(m,n)
                        s, t = int(neighbor[0]), int(neighbor[1])  # extracting coordinates of the neighbor

                        if IMG[s,t] == 1 and MARK[s,t] == 0:    #* if n(s,t) is pavement and MARK(s,t) in not visited
                            pixels_qty += 1
                            MARK[s,t] = 1   #* set MARK(s,t) as visited
                            if s < rows-1 and t < col-1:
                                n_st = {'x_cord': s, 'y_cord': t}         # saving x and y coordinates of the q(m,n) pixel to calculate the 8 neighbors
                                Q.append(n_st)  #* add n(n,t) into Q      
                        pass

                pixels_qty_in_component_list.append({'comp_number': connected_component_qty, 'qty':pixels_qty})

    writeTxtFile(pixels_qty_in_component_list, '2a')
    return MARK



def makeImageOfLargestComp(list_of_comp_pixels: list, largest1_indx: dict, largest2_indx: dict, _size: tuple):
    """ This is a supporting function that makes a binary image of the 2 largest connected components

    Parameters:
    
    list_of_comp_pixels: list
        A list containig the coordinates of the pixels that are present in each connected components
    largest1_indx: dict
        A dictionary that has the index of the 1st largest connected component 
    largest2_indx: dict
        A dictionary that has the index of the 2nd largest connected component 
    
    _size: tuple
        A tuple that contains the size of the original image.
    Returns
    -
    None
    
    """

    largest1 = list_of_comp_pixels[largest1_indx['comp_number']-1]
    largest2 = list_of_comp_pixels[largest2_indx['comp_number']-1]
    top_2_comp = [largest1, largest2]
    r, c = _size
    cc_top_2 = np.zeros((r,c))

    for large_comp in top_2_comp:
        for pxl in large_comp:
            x, y = pxl['x_cord'], pxl['y_cord']
            cc_top_2[x,y] = 1

    plt.imshow(cc_top_2); plt.show()
    io.imsave('cc-top-2.jpg', cc_top_2, check_contrast=False)


def detect_connected_components_sorted(MARK):
    """ This function is used to calculate a sorted list of the connected components from a binary image. 
    
    A connected component is a set of pixels that are adjecent to each other with the assumption of 8-adjecency.
    It takes the binary image obtained from task 2a and find the connected compoenets and store them in a array
    The array is then sorted based on the number of pixels each connected component has. 
    And it writes the sorted connected components information to a txt file named "cc-output-2b.txt"

    Parameters
    ----------
    IMG: np.array
        A binary image (obtained from the task 2a)
    Returns
    -------
    None

    """
    
    rows, col = MARK.shape
    unMARK = np.zeros((rows,col))     #* Step 1: set MARK as unvisited
    
    Q = []  #* Step 2: Empty queue-like array
    # -------------------------------------------------
    # Calculating the number of connected components
    connected_component_qty = 0
    pixels_qty_in_component_list = []    # the index of this array will tell the Sr# of connected component
    
    first_largest_comp_px = []
    second_largest_comp_px = []
    list_of_comp_pixels = []
    len_list_of_comp_pixels = []
    comp_pixels = []
    xx = []
    # -------------------------------------------------
    for x in range(rows-1):
        for y in range(col-1):
            px = MARK[x, y]
            
            
            if px == 1 and unMARK[x, y] == 0:
                unMARK[x,y] = 1

                connected_component_qty += 1
                
                # saving x and y coordinates of the q(m,n) pixel to calculate the 8 neighbors
                px_cord = {'x_cord': x, 'y_cord': y}
                comp_pixels = []
                comp_pixels.append(px_cord)

                Q.append(px_cord)
                pixels_qty = 1

                while len(Q)>0:
                    q_mn = Q[0]
                    Q.remove(q_mn)

                    eight_neighbors = find8Neighbours(q_mn)

                    for neighbor in eight_neighbors:
                        s, t = int(neighbor[0]), int(neighbor[1])  # extracting coordinates of the neighbor

                        if MARK[s,t] == 1 and unMARK[s,t] == 0:
                            pixels_qty += 1
                            unMARK[s,t] = 1
                            n_st = {'x_cord': s, 'y_cord': t}         # saving x and y coordinates of the q(m,n) pixel to calculate the 8 neighbors

                            # second_largest_comp_px.append(n_st)
                            comp_pixels.append(n_st)
                            
                            if s < rows-1 and t < col-1:
                                Q.append(n_st)
                        pass
                
                pixels_qty_in_component_list.append({'comp_number': connected_component_qty, 'qty':pixels_qty})
                list_of_comp_pixels.append(comp_pixels)

    
    sorted_list = pixels_qty_in_component_list
    sorted_list.sort(key=sortFn, reverse=True)

    writeTxtFile(sorted_list, '2b')
    makeImageOfLargestComp(list_of_comp_pixels, sorted_list[0], sorted_list[1], (rows, col))


def writeTxtFile(pxl_qty_list: np.array, task_number: str):
    """ This is a supporting function that writes the information of the connected components into a text file

    Parameters
    ----------
    pxl_qty_list: np.array
        An array of dictionary that contains the connected component number and the quantity of pixels in them
    task_number: str
        A string that defines the name of the txt file
    Returns
    -------
    None
    
    """

    with open('cc-output-'+ task_number +'.txt', 'w') as f:
        
        for item in pxl_qty_list:
            comp_num = item['comp_number']
            px_qty = item['qty']
            f.write(f'Connected Component { comp_num }, number of pixels = {px_qty}\n')
        
        f.write(f'Total number of connected components = {len(pxl_qty_list)}')

    pass


def sortFn(dict_unsorted: dict):
    """ A supporting function that helps in sorting of an array containing dictionaries based on the key value
    
    Parameters:
    
        dictionary wrt to which the sorting will be done
    Returns:
    
        value of the dictionary item against "qty" key

    """

    return dict_unsorted['qty']


#Calling functions below

    
# TASK M1
map_filename = input('enter image path file: ')
    
# Task M1a
red_b = find_red_pixels(map_filename)
    
# Task M1b
cyan_b = find_cyan_pixels(map_filename)
    

 #* TASK M2 
b_image_filename = 'map-red-pixels.jpg'
b_image = plt.imread(b_image_filename)
b_image = 1 * b_image >= 127.5

 # task M2a
mark = detect_connected_components(b_image)
    
# task M2b
detect_connected_components_sorted(mark)
