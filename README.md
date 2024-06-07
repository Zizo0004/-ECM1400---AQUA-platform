# AQUA (Air Quality Analytics) Platform 

## Introduction
AQUA serves as an air pollution data analytics solution, catering to policy makers and public servants responsible for monitoring pollution levels across different areas of the country. [Full Specfication](https://vle.exeter.ac.uk/pluginfile.php/3682347/mod_label/intro/ECM1400_reassessment_2023.pdf). I couldn't locate the original specification, this is thhe revise version.

## Dataset Overview
The air pollution dataset provided spans one year (2021) and includes hourly measurements for three pollutants: nitric oxide (NO), PM10 inhalable particulate matter (≤ 10µm), and PM2.5 inhalable particulate matter (≤ 2.5µm). The data is sourced from three monitoring sites in London: Marylebone Road, N. Kensington, and Harlington, each providing 8760 data points. The dataset is structured in CSV format, with columns representing date, time, NO levels, PM10 levels, and PM2.5 levels.

### Monitoring Sites
- **Marylebone Road**

  - Site Code: MY1
- **N. Kensington**

  - Site Code: KC1
- **Harlington**

  - Site Code: HRL

## Project Specification
The AQUA platform encompasses two key modules: Pollution Reporting (PR) and Real-time Monitoring (RM).

### Pollution Reporting (PR) Module
The PR module is tasked with providing relevant pollution level information from different monitoring stations. Users can generate statistics at various aggregation levels (hourly, daily, monthly, etc.) using temporal data analysis techniques.

#### Coding Tasks
Module file: `reporting.py`

Functions:
- `daily_average(data, monitoring_station:str, pollutant:str)`: Returns daily averages for a specific pollutant and monitoring station.
- `daily_median(data, monitoring_station:str, pollutant:str)`: Returns daily median values for a specific pollutant and monitoring station.
- `hourly_average(data, monitoring_station:str, pollutant:str)`: Returns hourly averages for a specific pollutant and monitoring station.
- `monthly_average(data, monitoring_station:str, pollutant:str)`: Returns monthly averages for a specific pollutant and monitoring station.
- `peak_hour_date(data, date:str, monitoring_station:str, pollutant:str)`: Returns the hour of the day with the highest pollution level and its corresponding value for a given date.

### Real-time Monitoring (RM) Module
The RM module retrieves real-time analytics from the London Air API, providing users with up-to-date statistics for different monitoring stations and pollutants. 

#### Coding Tasks
Module file: `monitoring.py`


### User Interface
The AQUA system utilizes a text-based interface for user interaction. Upon initialization, the main menu presents options for accessing the PR module, RM module, displaying About text, and quitting the application.

#### Coding Tasks
Module file: `main.py`

Functions:
- `main_menu()`: Displays the main menu, allowing users to navigate through different options.
- `reporting_menu()`: Allows users to perform analyses described in the PR module and navigate through options.
- `monitoring_menu()`: Allows users to perform tasks described in the RM module and navigate through options.
- `about()`: Prints module code and candidate number before returning to the main menu.
- `quit()`: Terminates the program.

