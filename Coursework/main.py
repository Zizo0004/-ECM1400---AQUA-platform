import reporting
import intelligence


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, util #COULD NOT INSTALL THIS LIBRARY ON VS CODE DUE TO PYTHON 3.11 ERROR. Code was completed on jupiter notebook and transferred to vs code

def reporting_menu():
    """ This function gathers all functions from reporting.py to display aggregate data
        Parameter:
        no parameters
        
        Return:
        returns the daily,monthly,hourlry average , daily median , peak_hour , count_missing_data, fill_missing_data for a given csv file"""
    #ask user to input a station
    function_choices = input('What stats do you want to view? 1) daily_average , 2) daily_median , 3) hourly_average , 4) peak_hour , 5) monthly_average , 6) count_missing_data , 7) fill_missing_data: ').lower()
    
    if function_choices == 'daily_average':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ').upper()
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ').lower()
        #ask the user to type in data
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        results = reporting.daily_average(data, station_input, pollutant_input)
        #prints desired outcome
        print(len(results))
        print(results)
        #---------------------------------------------------------------------------#
    if function_choices == 'daily_median':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ').upper()
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ').lower()
        #ask the user to type in data
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        results = reporting.daily_median(data, station_input, pollutant_input)
        #prints desired outcome
        print(results)
        #--------------------------------------------------------------------------#
    if function_choices == 'hourly_average':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ').upper()
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ').lower()
        #ask the user to type in data
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        results = reporting.hourly_average(data, station_input, pollutant_input)
        #prints desired outcome
        print(results)
       #---------------------------------------------------------------------------#
    if function_choices == 'peak_hour':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ').upper()
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ').lower()
        #ask the user to type in data
        date_input = input('Pick a date: ')
        #ask user to input a date
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        results = reporting.peak_hour_date(data,date_input,station_input, pollutant_input)
        #prints desired outcome
        print(results)
       #-----------------------------------------------------------------------------#
    if function_choices == 'monthly_average':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ')
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ')
        #ask the user to type in data
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        results = reporting.monthly_average(data, station_input, pollutant_input)
        #prints desired outcome
        print(results)
    #-----------------------------------------------------------------------------------#
    if function_choices == 'count_missing_data':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ')
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ')
        #ask the user to type in data
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        results = reporting.count_missing_data(data, station_input, pollutant_input)
        #prints desired outcome
        print(results)
    #-----------------------------------------------------------------------------------#
    if function_choices == 'fill_missing_data':
        station_input = input('Pick from the following stations: MY1, KC1 , HRL: ')
        #ask user to input a pollutant
        pollutant_input = input('Pick from the following stations: no, pm10, pm25: ')
        #ask the user to type in data
        data = input('Enter the phrase Data: ')
        #store daily_average function in results 
        new_value = input('Enter a numercial number to fill in the missing data: ')
        results = reporting.fill_missing_data(data,new_value,station_input, pollutant_input)
        #prints desired outcome
        print(results)
def intelligence_menu():
    """This function uses previous functions to output results from Task 1 to Task 2
    
    Parameters
    
    no parameters are taken in because we are calling the function

    Returns
    
    A 2-D array containing the binary image of red pixels
    A 2-D array containing the binary image of cyan pixels
    txt file containing conntected compononented sorted in decreasing order   
    
    
    """
    
    #retrieve image path, map.png
    map_filename = input('Enter the path to the map image')
    # red pixels stored in red_image, function called
    red_image= intelligence.find_red_pixels(map_filename)
    #cyan pixels stored in cyan_image, function called
    cyan_image= intelligence.find_cyan_pixels(map_filename)
    print(red_image)
    print(cyan_image)
    
    #saving red pixel array to call function from 2a
    IMG_filename = 'map-red-pixels.jpg'
    IMG = plt.imread(IMG_filename)
    IMG = 1 * IMG >= 127.5
    
    mark = intelligence.detect_connected_components(IMG)
    intelligence.detect_connected_components_sorted(mark)

    
 

def monitoring_menu():
    print('Could not call function because API was down. It crashed the program when i called functions from mointoring.py')

def about():
    """ This function takes no parameters
        return my 6 digit student code and module code"""
    #outputs ECM1400
    print('ECM1400')
    #outputs 255877
    print('255877')

def quit():
    """This function takes no parameters
       when called it reassigns program_on to False stopping the while loop"""
    program_on = False


def main_menu():
    """This functions takes no parameters 
       allows users to view the reporting.py, intellgeience.py and mointoring.py """
    #while loop used to contionusly run program until keyword break used
    program_on = True
    while program_on:
        #gives users options to navigate the menu
        choices = ('''
• R - Access the PR module
• I - Access the MI module
• M - Access the RM module
• A - Print the About text
• Q - Quit the application 

''')
        user_input = input(choices).upper()
        #control on user_input
        if user_input == "R":
            #reporting function is called
            reporting_menu()
        elif user_input =='I':
            #intelligence function is called
            intelligence_menu()
        elif user_input == 'M':
            #no output due to api error crashing program
            monitoring_menu()
        elif user_input =='A':
            # information containing student id and module code printed
            about()
        elif user_input == "Q":
            #terminates program
            quit()
            break


#Main menu function called
print(main_menu())