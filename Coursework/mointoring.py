"""
This is the main script file. It asks the user to enter site code, species code, start and end date.
From the RM Validation Module, the entered data is validated and if correct, the data is fetched from the API
and displayed to the user
"""


from rm_validator import *
from prettytable import PrettyTable #Could not install this specific library to vs code!

seed1 = {'site': "TD0", 'specie': 'CO', 'start_date_str': '2017-01-01', 'end_date_str': '2017-01-10'}
seed2 = {'site': "BG1", 'specie': 'NO2', 'start_date_str': '2017-01-01', 'end_date_str': '2017-01-10'}


rm = RMValidator() 

def getEachDayStats(params: dict) -> np.array:
    """ A supporting function used to scrap the pollutant values from each hour of the date range
    From the set of entered parameters, the data is fetched from the API and stored in an array of dictionaries.
    the key of each dictionary in that array is a specific date. and the value is an array that holds the data for each hour of that day
    If there is no value found for any hour, default value 0.0 is used.

    Parameters
    ----------
    params: dict
        A disctionay that constains value of site_code, species_code, start_date_str, end_date_str, use_seed
        These are used to get the data from API
    Returns
    -------
    nd.array
        an array that contains the hourly value of the species between the entered date range

    """
    
    site_code = params['site_code']
    species_code = params['species_code']
    start_date_str = params['start_date_str']
    end_date_str = params['end_date_str']
    use_seed = params['use_seed']
    
    url = f"https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date_str}/EndDate={end_date_str}/Json"

    if not use_seed:    # if the user want to get fresh data from the API
        api_response = req.get(url, params={'encoding': 'utf-8'})
        if api_response.status_code == 200: # if the API response is successful
            data = api_response.json()
        else: # if the API response is not successful
            print(f"Error {api_response.status_code}. Using the seed file")
            use_seed = True # setting use_seed True and using the pre-loaded data

    if use_seed:
        content = open("./auxillary-dir/RAWDATA.txt", 'r')  # reading the pre-loaded data from txt file
        data = literal_eval(content.read())['RawAQData']    # converting the string datatype to the literal datatype (object in this case)
        
        # as the API is not working, using the values tha are available in the pre-loaded data file
        site_code = data['@SiteCode']
        species_code = data['@SpeciesCode']
        start_date_str = data['Data'][0]['@MeasurementDateGMT'].split(" ")[0]   # string format of the date "YYY-MM-DD"
        end_date_str = data['Data'][-1]['@MeasurementDateGMT'].split(" ")[0]    # string format of the date "YYY-MM-DD" 

        # converting the string format of the date into date format
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        # calculating the number of days from the start_date to end_date
        number_of_days = (end_date - start_date).days + 1
        
        daily_value = []    # an empty array that will store the the values of each hour of each day
        
        temp_date = start_date  # setting start_date as a temp_date. This temp_date will be updated below
        
        for d in range(number_of_days): # using for loop to save the data of each day fro start_date to end_date
            
            # below is a single liner for loop. it takes the value of each hour and stores it in an array.
            # each element of the array represents the value against the hour (starting from 00:00:00 to 23:00:00)
            # this array is stored as a dictionay and the key is the date value
            daily_value.append({str(temp_date): [(float(d['@Value']) if d['@Value']!='' else 0.0) for d in data['Data'] if d['@MeasurementDateGMT'].split(" ")[0]==str(temp_date)]})
            
            temp_date = temp_date + timedelta(days=1) # adding 1 day to the temp_date. this will fetch the data of the next day
        
    return daily_value


def dailyAvgValue(site_code: str, species_code: str, start_date_str: str, end_date_str: str, use_seed: bool =False, display_table=True):
    """ A function used to calculate the daily average of the specie values.

    Parameters:

    site_code: str
        site code entered by the user 
    species_code: str
        case-sensitive species code
    start_date_str: str
        the date is in the string datatype and the format is "YYYY-MM-DD"
    end_date_str: str
        the date is in the string datatype and the format is "YYYY-MM-DD"
    use_seed: bool
        Option of using the pre-loaded seed data if the API is not working. (default: False)
    Returns:

    nd.array
        an array that contains the daily average value of the species

    """

    entered_params = {'site_code': site_code, 'species_code': species_code, 'start_date_str': start_date_str, 'end_date_str': end_date_str, 'use_seed': use_seed}
    daily_value = getEachDayStats(params=entered_params)

    daily_avg = []  # an empty array that will store the daily average value of each day
    for dic in daily_value:
        for key, val in dic.items():
            daily_avg.append({key: round(np.average(val), 2)})
    
    if display_table:
        table = PrettyTable()
        table.title = f'Daily Average value of {species_code}'
        col_headers = ['Date', 'Avg Value']
        for c in col_headers:
            table.add_column(c, [])

        for ele in daily_avg:
            date_value = str(list(ele.keys())[0])
            avg_value = str(list(ele.values())[0])
            table.add_row([date_value, avg_value])

        print(table)

    return daily_avg


def maxPollutantDay(site_code: str, species_code: str, start_date_str: str, end_date_str: str, use_seed: bool =False):
    
    entered_params = {'site_code': site_code, 'species_code': species_code, 'start_date_str': start_date_str, 'end_date_str': end_date_str, 'use_seed': use_seed}
    daily_value = getEachDayStats(params=entered_params)

    d_avg = dailyAvgValue(site_code, species_code, start_date_str, end_date_str, use_seed, display_table=False)
    
    # Calculating the max value from the average of rach day list and finding its index
    indx, mx = 0, 0
    for i, item in enumerate(d_avg):
        val = list(item.values())[0]
        indx, mx = ([i, val] if val > mx else [indx, mx])

    # extracting hourly values of the max polluted day
    max_polluted_day = daily_value[indx]
    date_of_peak_day = list(max_polluted_day.keys())[0]

    all_hours_of_peak_day = list(max_polluted_day.values())[0]
    peak_hour_val = max(all_hours_of_peak_day)
    peak_hour_indx = all_hours_of_peak_day.index(peak_hour_val)

    # creating pretty table for result display
    table = PrettyTable()
    table.title = f'The Most Polluted Day is {date_of_peak_day}'
    col_headers = ['Peak Hour', 'Pollution Value']
    
    for c in col_headers:
        table.add_column(c, [])

    peak_hour = f"{peak_hour_indx}:00:00"
    peak_hour_val_str = str(peak_hour_val)
    table.add_row([peak_hour, peak_hour_val_str])

    print(table)

    peak_hour_data = {'date': date_of_peak_day, 'hour': peak_hour, 'peak_value': peak_hour_val}

    return peak_hour_data


def monthlyAvgValue(site_code: str, species_code: str, start_date_str: str, end_date_str: str, use_seed: bool =False) -> np.array:

    pass    

d_avg = dailyAvgValue(site_code=seed1['site'], species_code=seed1['specie'], start_date_str=seed1['start_date_str'], end_date_str=seed1['end_date_str'], use_seed=True)
max_pollutant = maxPollutantDay(site_code=seed1['site'], species_code=seed1['specie'], start_date_str=seed1['start_date_str'], end_date_str=seed1['end_date_str'], use_seed=True)


def hourly_data(site_code:str,species_code:str,start_date:None,end_date:None):
    import requests
    import datetime
    import pandas as pd
    #This will output today's data if no data was given
    start_date = datetime.date.today() if start_date is None else start_date
    #In the case where no data was given, it was will provide the end date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    #retreiving data from the API
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    
    #to make sure user's input matches the url
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    #uses the get function to retreive data
    res = requests.get(url)
    #stores data in json format
    data = res.json()
    #accessing the 'data' key
    data = data['RawAQData']['Data']
    #using list comprehesion to provide the index for each date and corressponding value
    aligned_data= {i: v for i, v in enumerate(data)}
    #create a pandas dataframe to display information
    data_table = pd.DataFrame(aligned_data)
    #use function T to re-align coloumns and rows
    data_table= data_table.T
    #Rename coloumns to allow the user to understand the dataframe
    data_table.rename(columns={'@MeasurementDateGMT':'Date and Time    ' ,'@Value': 'Value'},inplace=True)
    #store Value column in a variable
    value_column = data_table['Value']
    #loop through each index and corressponding value
    for index, value in enumerate(value_column):
        #checking to see if the value is empty
        if value == '':
            #empty value is dropped and row is dropped
            data_table.drop(index, inplace=True) 
        else:
            pass   

    #returns dataframe
    return data_table