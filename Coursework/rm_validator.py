
import requests as req
import pandas as pd
import json, sys
from ast import literal_eval
import numpy as np
from datetime import datetime, date, timedelta


class RMValidator:
    """
    This class validates the input arguments entered by the user.
    It searches wheteher the values entered by the user are available in the API or not.
    If the user has entered correct value, the respoctive class method will return True, otherwise False
    """

    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    
    def __init__ (self):

        self.control_data_keys: list = ['@SiteName', '@SiteCode', '@DateOpened', '@DateClosed']
        self.control_data_list: list = []
        self.control_data_filename: str = ""
        
        self.group_name: str = ""
        
        self.allowed_date_range: list = []
        
        self.species_code_list = ["CO", "NO2" "O3", "PM10", "PM25", "SO2"]
        pass

    def getInputControlData(self, group_name: str = 'London', default: bool = False) -> None :
        """This method gets the data from the API which is used for user input validation
        It updates the class attributes that are used in several class methods for implementing the validation finctionality

        Parameters:
        
        group_name: str
            Group name of area whose data is to be used in the script (default: 'London')
        default: bool
            
        Returns:
        None

        """

        self.group_name = group_name
        if not default: # if the user wants to get new data from the API
            # getting response from API
            api_url = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={self.group_name}/Json"
            api_response = req.get(api_url, params={'encoding': 'utf-8'})

        if not default and api_response.status_code == 200: # if response is successful, above 400 == error
            print(" Data successfully fetched from the API")
            data = api_response.json()['Sites']['Site']     # convert the response into json format

        else: # if api response is not successful, using the default txt file with pre-loded data in it
            print(f"Using default txt file")
            content = open("./auxillary-dir/apidata-london.txt", 'r')
            data = literal_eval(content.read()) # converting the string format into list datatype (because list of dictionaries is stored in the txt file)

            for i in range(len(data)):  # saving data from the selected keys in a separate array 
                self.control_data_list.append( {key: data[i][key] for key in self.control_data_keys })
            
            df = pd.DataFrame(self.control_data_list)    # converting the array to dataframe object

            self.control_data_filename = './auxillary-dir/control-data-'+ self.group_name +'.txt' # txt file path to store the filtered data as a dataframe table
            
            with open(self.control_data_filename,'w') as outfile:
                df.to_string(outfile,columns=self.control_data_keys)    # saving the dataframe object into a txt file as a table


    def checkSiteCode(self, site_code: str) -> bool :
        """ This method checks if the entered site code is correct or not.
        It fetches the entered value from the API response data

        Parameters:
    
        site_code: str
            site code entered by the user 

        Returns:
        
        bool
            True if the site code is found in the validation reference data else False

        """

        return True if any(d['@SiteCode'] == site_code for d in self.control_data_list) else False
        

    def findOpenCloseDate(self, site_code: str) -> None:
        """  For the entered site code, This method finds and prints the start and end date range.
        If the end date is not available, current date is stored.
        ather it updates the class attribute self.allowed_date_range and prints the allowable date range


        Parameters:
        
        site_code: str
            site code entered by the user 
        Returns:
        
        nothing

        """
        # finding the index of the dictionary that has the entered site code
        indx = [i for i, d in enumerate(self.control_data_list) if site_code in d.values()][0]

        # fetching open and close date against the index
        open_date = self.control_data_list[indx]['@DateOpened'].split(" ")[0]
        close_date = self.control_data_list[indx]['@DateClosed'].split(" ")[0]
        close_date = self.current_date if close_date == '' else close_date

        self.allowed_date_range = [open_date, close_date]

        # displaying the allowblae date range to the user
        print("\nChoose date between the following range: (Date format: YYYY-MM-DD)")
        print(f"{open_date} \t-to-\t {close_date}")


    def checkEnteredDate(self, entered_date: str) -> bool:
        """ This method checks whether the entered start/end date is correct or not.

        Parameters
        ----------
        entered_date: str
            the date is in the string datatype and the format is "YYYY-MM-DD"
        Returns
        -------
        bool
            True if the entered date is within the allowable range else False

        """

        y, m, d = entered_date.split("-")   # splitting the string date into year, month, and date
        d = date(int(y), int(m), int(d))    # converting into int format
        
        return True if (self.allowed_date_range[0] <= entered_date <= self.allowed_date_range[1]) else False
        
    
    def checkSpecieCode(self, species_code: str) -> bool:
        """ This method checks whether the entered species code is correct or not.

        Parameters
        ----------
        species_code: str
            case-sensitive species code
        Returns
        -------
        bool
            True if the if the entered species code is in the species_code_list else False

        """
        return True if species_code in self.species_code_list else False


if __name__ == "__main__":
    #* if this script is run, it will execute the main.py file
    exec(open("main.py").read())
