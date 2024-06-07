import numpy as np
import pandas as pd

def daily_average(data, monitoring_station, pollutant:str):
    """ Takes data, station name and pollutant to return the daily_average value for a specific station and pollutant
       Parameters:
       data:str , uses data from monitoring_station
       monitoring_station:str , users inputs a station to match the .csv file
       pollutant:str , user inputs pollutants from no,pm10 or pm25

       Return:
       a list of the daily average values (365 values)
    """
    #check too see if monitoring_station is valid
    if monitoring_station == 'HRL':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London Harlington.csv')
        #iterates over 'no data' and replaces it with nan values
        data.replace('No data', np.nan, inplace=True)
        #nan value dropped from row
        data = data.dropna()

        #change type of columns to do calculations
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        if pollutant == "no":
            #uses grouby().mean function is get the sum of the values divided by 24
            Daily_average = data.groupby('date').no.mean()
        elif pollutant =='pm10':
            Daily_average = data.groupby('date').pm10.mean()
        elif pollutant =='pm25':
            Daily_average = data.groupby('date').pm25.mean()
        else:
            print('invalid input, try again')
        #returns daily average values as a list
        
        return(list(Daily_average))
    
    
    if monitoring_station == 'MY1':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv(r'C:\Users\ziyad\OneDrive\Documents\Coursework\Pollution-London Marylebone Road.csv')
        #'no data' values are replaced with nan
        data.replace(['No data'], np.nan, inplace=True)
        #change type of columns to do calculations
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)
        

        if pollutant == "no":
            Daily_average = data.groupby('date').no.mean()
            
        elif pollutant =='pm10':
            Daily_average = data.groupby('date').pm10.mean()
        elif pollutant =='pm25':
            Daily_average = data.groupby('date').pm25.mean()
        #if no other pollutant given, raise a error
        else:
            print('invalid input, try again')
        return(list(Daily_average))


    
    elif monitoring_station == "KC1":
        #Read csv file and assign it to a dataframe
        data = pd.read_csv(r'C:\Users\ziyad\OneDrive\Documents\Coursework\Pollution-London N Kensington.csv')
        #no data is converted to nan, and is dropped
        data.replace('No data', np.nan, inplace=True)
        data = data.dropna()
        #value columns changed to float for calculations
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        if pollutant == "no":
            Daily_average = data.groupby('date').no.mean()
        elif pollutant =='pm10':
            Daily_average = data.groupby('date').pm10.mean()
        elif pollutant =='pm25':
            Daily_average = data.groupby('date').pm25.mean()
        else:
            print('invalid input, try again')
            #returns list of daily values
        return (list(Daily_average))
    #raise a error if no other station is given
    else:
        print("Invalid input! Please choose from the following stations, MY1, KC1 or HRL")
        


def daily_median(data, monitoring_station, pollutant):
    """
    This function takes in data, mointoring station and pollutant to return daily median values

    Parameters:
    data:str, data is stored in a pandas dataframe
    monitoring_station:str, user inputs station of interest
    pollutant:str, user chooses a pollutant

    Return:
    an array of daily median values (365 values) for a given dataframe
    """
    

    if monitoring_station == 'HRL':
        #Reads csv file and assign it to a pandas DataFrame
        data = pd.read_csv('Pollution-London Harlington.csv')
        #no data values are replaced with nan values
        data.replace('No data', np.nan, inplace=True)
        #drops nan values
        data = data.dropna()
        #numerical string values converted to float
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        if pollutant == "no":
            #iterates over data coloumn and finds daily median values which is stored in median
            median = data.groupby('date').no.median()
        elif pollutant =='pm10':
            median = data.groupby('date').pm10.median()
        elif pollutant =='pm25':
            median = data.groupby('date').pm25.median()
        else:
            print('invalid input, try again')
        return(list(median))
    
    
    if monitoring_station == 'MY1':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London Marylebone Road.csv')
        #no data values are replaced with nan values
        data.replace(['No data'], np.nan, inplace=True)
        #numerical string values converted to float
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)
        
        

        if pollutant == "no":
            # Finds daily median values from the date column
            median = data.groupby('date').no.median()
            
        elif pollutant =='pm10':
            median = data.groupby('date').pm10.median()
        elif pollutant =='pm25':
            median = data.groupby('date').pm25.median()
        else:
            print('invalid input, try again')
        #return an array of daily median
        return(list(median))


    
    elif monitoring_station == "KC1":
        #Read csv file and assign it to a dataframe
        data = pd.read_csv(r'C:\Users\ziyad\OneDrive\Documents\Coursework\Pollution-London N Kensington.csv')
        data.replace('No data', np.nan, inplace=True)
        data = data.dropna()
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        if pollutant == "no":
            median = data.groupby('date').no.median()
        elif pollutant =='pm10':
            median = data.groupby('date').pm10.median()
        elif pollutant =='pm25':
            median = data.groupby('date').pm25.median()
        else:
            print('invalid input, try again')
        return (list(median))

    else:
        print("Invalid input! Please choose from the following stations, MY1, KC1 or HRL")



def hourly_average(data, monitoring_station, pollutant):
    """ This function iterates over each hour in the dataframe and finds the hourly average for from hrs 0-24 from csv file
    
    Parameters:

    data:str, data stores the dataframe containing the csv file
    mointoring_station:str, user inputs a station of their chosen
    pollutant:str, user inputs a pollutant assigned to mointoring_station

    Return:
    an array of hourly averages for a given dataframe
    """
    
    ## Your code goes here

    if monitoring_station == 'HRL':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London Harlington.csv')
        #no data values replaced with nan values
        data.replace('No data', np.nan, inplace=True)
        #nan values dropped 
        data = data.dropna()
        #value columns type changed from string to float
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        if pollutant == "no":
            #groupby('time') iterates over each hour and store an hourly average from 0-24 hours
            hourly_average = data.groupby('time').no.mean()
        elif pollutant =='pm10':
            hourly_average = data.groupby('time').pm10.mean()
        elif pollutant =='pm25':
            hourly_average = data.groupby('time').pm25.mean()
        else:
            print('invalid input, try again')
        #returns an array of hourly average
        
        return(list(hourly_average))
    
    
    if monitoring_station == 'MY1':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London Marylebone Road.csv')
        #no data vlaues changed to nan
        data.replace(['No data'], np.nan, inplace=True)
        #each column type changed to float for calculations
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)
        
        

        if pollutant == "no":
            hourly_average = data.groupby('time').no.mean()
        elif pollutant =='pm10':
            hourly_average = data.groupby('time').pm10.mean()
        elif pollutant =='pm25':
            hourly_average = data.groupby('time').pm25.mean()
        else:
            print('invalid input, try again')
        
        return((list(hourly_average)))


    
    elif monitoring_station == "KC1":
        #Read csv file and assign it to a dataframe
        data = pd.read_csv(r'C:\Users\ziyad\OneDrive\Documents\Coursework\Pollution-London N Kensington.csv')
        data.replace('No data', np.nan, inplace=True)
        data = data.dropna()
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        if pollutant == "no":
            hourly_average = data.groupby('time').no.mean()
        elif pollutant =='pm10':
            hourly_average = data.groupby('time').pm10.mean()
        elif pollutant =='pm25':
            hourly_average = data.groupby('time').pm25.mean()
        else:
            print('invalid input, try again')
        
        return(list(hourly_average))

    else:
        print("Invalid input! Please choose from the following stations, MY1, KC1 or HRL")








def peak_hour_date(data, date, monitoring_station,pollutant):
    """ This function iterates over each hour in the dataframe and finds the hour with the largest pollutant value in a given dataframe
    
    Parameters:

    data:str, data stores the dataframe containing the csv file
    date:str format(YY-MM-DD), user inputs a date to get the pollutant with the highest value 
    mointoring_station:str, user inputs a station of their chosen
    pollutant:str, user inputs a pollutant assigned to mointoring_station

    Return:
    prints the hour associated with the highest pollutant value and the value itself
    """
    
    ## Your code goes here
    if monitoring_station == 'HRL':
    #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London Harlington.csv')
        # no data values converted to nan
        data.replace('No data', np.nan, inplace=True)
        # nan values are dropped
        data = data.dropna()
        #value columns type changed to float
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        # Use pandas to extract the hour and pollutant value for the specified date and monitoring station
        df = data[(data['date'] == date)]
        df = df[['time', pollutant]]

        # Find the hour with the highest pollutant value
        hour = df['time'].loc[df[pollutant].idxmax()]

        # Return the hour and pollutant value
        return hour,df[pollutant].max()

            

    if monitoring_station == 'MY1':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London Marylebone Road.csv')
        data.replace(['No data'], np.nan, inplace=True)
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)
        
        
        df = data[(data['date'] == date)]
        df = df[['time', pollutant]]

        # Find the hour with the highest pollutant value
        hour = df['time'].loc[df[pollutant].idxmax()]

        # Return the hour and pollutant value
        return hour,df[pollutant].max()


    if monitoring_station == 'KC1':
        #Read csv file and assign it to a dataframe
        data = pd.read_csv('Pollution-London N Kensington.csv')
        data.replace('No data', np.nan, inplace=True)
        data = data.dropna()
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)


        df = data[(data['date'] == date)]
        df = df[['time', pollutant]]

        # Find the hour with the highest pollutant value
        hour = df['time'].loc[df[pollutant].idxmax()]

        # Return the hour and pollutant value
        return hour,df[pollutant].max()







def monthly_average(data, monitoring_station, pollutant):
    
    """This function iterates over each date in the dataframe and returns the monthly average value for each month
    
    Parameters:

    data:str, data stores the dataframe containing the csv file
    mointoring_station:str, user inputs a station of their chosen
    pollutant:str, user inputs a pollutant assigned to mointoring_station

    Return:
    monthly average values for a given dataframe
    """
    
    ## Your code goes here
    if monitoring_station == 'MY1':
        data = pd.read_csv('Pollution-London Marylebone Road.csv')
        #no data values replaced with nan values
        data.replace('No data', np.nan, inplace=True)
        #nan values removed
        data = data.dropna()
        # value columns type changed to float for calculating
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)
    
        data['date'] = pd.to_datetime(data['date']) # changes date format

        monthly_avg = data.groupby(data["date"].dt.month)[pollutant].mean() #* grouby method accesses date and pollutant column to caluclate monthly average
        monthly_avg_list = monthly_avg.tolist() # turns values into a list
        return monthly_avg_list 
        

    elif monitoring_station == 'HRL':
        #csv read and stored in data
        data = pd.read_csv('Pollution-London Harlington.csv')
        data.replace('No data', np.nan, inplace=True)
        data = data.dropna()
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        data['date'] = pd.to_datetime(data['date'])

        monthly_avg = data.groupby(data["date"].dt.month)[pollutant].mean()
        monthly_avg_list = monthly_avg.tolist()
        return monthly_avg_list
        

    elif monitoring_station == 'KC1':
        data = pd.read_csv('Pollution-London N Kensington.csv')
        data.replace('No data', np.nan, inplace=True)
        data = data.dropna()
        data['no']= data['no'].astype(str).astype(float)
        data['pm10']= data['pm10'].astype(str).astype(float)
        data['pm25']= data['pm25'].astype(str).astype(float)

        data['date'] = pd.to_datetime(data['date'])

        monthly_avg = data.groupby(data["date"].dt.month)[pollutant].mean()
        monthly_avg_list = monthly_avg.tolist()
        return monthly_avg_list




def count_missing_data(data,  monitoring_station,pollutant):
    """ This function iterates every column and counts the occurrences of 'nan' entries
    
    Parameters:

    data:str, data stores the dataframe containing the csv file
    mointoring_station:str, user inputs a station of their chosen
    pollutant:str, user inputs a pollutant assigned to mointoring_station

    returns:
    array containing the number of times nan was found in the dataframe
    """
    
    ## Your code goes here
    if monitoring_station == 'HRL':
        #reads csv file and stores values in a dataframe
        data = pd.read_csv('Pollution-London Harlington.csv')
        #no data values converted to nan
        data.replace('No data', np.nan, inplace=True)
        #isnull function identifies nan values, and sum() function increments the occurrences of nan into missing_values
        missing_values = data[pollutant].isnull().sum()
        return missing_values
    
    elif monitoring_station =='KC1':
        data = pd.read_csv('Pollution-London N Kensington.csv')
        data.replace('No data', np.nan, inplace=True)


        missing_values = data[pollutant].isnull().sum()
        return missing_values

    elif monitoring_station =='MY1':
        data = pd.read_csv(r'C:\Users\ziyad\OneDrive\Documents\Coursework\Pollution-London Marylebone Road.csv')
        data.replace('No data', np.nan, inplace=True)


        missing_values = data[pollutant].isnull().sum()
        return missing_values






def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """This function finds all no data entries found and replaces value with the parameter new_value into the dataframe
    
    Parameters:
    data:str, data is assigned to the dataframe
    new_value:float, user decides what value to replace the missing entries in the dataframe
    mointoring_station:str, user inputs a station
    pollutant:str, user inputs a pollutant 
    """
    
    ## Your code goes here
    if monitoring_station == 'HRL':
        #reads csv file into a dataframe
        data = pd.read_csv('Pollution-London Harlington.csv')
        #no data entries replaced by nan values
        data.replace('No data', np.nan, inplace=True)
        #accessing the polluntant column in the dataframe to fill missing data with "new_value" parameter
        data[[pollutant]] = data[[pollutant]].fillna(new_value)
        return data
    
    elif monitoring_station =='KC1':
        data = pd.read_csv('Pollution-London N Kensington.csv')
        data.replace('No data', np.nan, inplace=True)


        data[[pollutant]] = data[[pollutant]].fillna(new_value)
        return data

    elif monitoring_station =='MY1':
        data = pd.read_csv(r'C:\Users\ziyad\OneDrive\Documents\Coursework\Pollution-London Marylebone Road.csv')
        data.replace('No data', np.nan, inplace=True)


        data[[pollutant]] = data[[pollutant]].fillna(new_value)
        return data






