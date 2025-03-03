## Importing the required modules for the function
import csv 
from functools import reduce,partial

## Defining the function process_sensor_pipeline
## with the filename as the argument
## The function reads the sensor data from the file
## and processes the data to convert the distance
def process_sensor_pipeline(filename:str):
    """
    This Outer function reads the sensor data from the file
    and processes the data to convert the distance
    from inches to centimeters. The function then
    filters the sensor data based on a threshold
    distance of 35 cm and calculates the average
    distance of the filtered data.

    Args:
        filename (str): The path to the sensor data file.
    Returns:
        None: The function does not return any value.
    """
    def read_sensor_data(filename : str) -> list[dict]:
        """Reads sensor data from a CSV file and returns a list of dictionaries.

        Args:
            filename (str): The path to the CSV file containing sensor data.

        Returns:
            list[dict]: A list of dictionaries containing sensor data.
        """
        ## Using a try-except block to handle file not found error
        try:
            ## Opening the file in read mode
            with open(filename,'r') as data_file:
                sensor_data_list = []
                
                sensor_data = csv.reader(data_file) ## Using the csv module to read the data
                header = next(sensor_data) ## Getting the header of the CSV file
                
                ## Iterating over the sensor data and creating a list of dictionaries
                
                for record in sensor_data:
                    sensor_data_list.append({
                        header[0] : int(record[0]),
                        header[1] : float(record[1]),
                        header[2] : record[2]
                    })
                ## Returning the list of dictionaries
                return sensor_data_list
            
        ## Handling the FileNotFoundError exception
        except FileNotFoundError:
            print("Pass a Valid filename!!!!")
            return []
        
        except ValueError:
            print("Invalid sensor id or distance!!!!")
            return []
        
    def inches_to_cm(inches : float) -> float:
        """Converts inches to centimeters.

        Args:
            inches (float): The distance in inches.

        Returns:
            float: The distance in centimeters.
        """
        return inches * 2.54

    def process_reading(reading : dict) -> dict:
        """Converts the distance in a sensor reading from inches to centimeters.

        Args:
            reading (dict): A dictionary containing sensor reading data.

        Returns:
            dict: A dictionary containing sensor reading data with the distance converted to centimeters.
        """
        reading_copy = reading.copy()
        reading_copy['distance'] = inches_to_cm(reading_copy['distance'])
        return reading_copy

    def threshold_filter(threshold : float, reading:dict ) -> bool:
        """Filters sensor readings based on a threshold distance.

        Args:
            threshold (float): The threshold distance in centimeters.
            reading (dict): A dictionary containing sensor reading data.

        Returns:
            bool: True if the distance in the reading is greater than or equal to the threshold, False otherwise.
        """
        return reading['distance'] >= threshold


    def average_distance(readings : list) -> float:
        """Calculates the average distance from a list of readings.

        Args:
            readings (list): A list of distances.

        Returns:
            float: The average distance.
        """
        ## Using the reduce function to calculate the sum of the distances
        if not readings:
            ## If the list of readings is empty, return a message
            return "No valid readings!!!!. Enter valid readings"
        
        accumulated_distance = reduce(lambda x,y : x+y, readings) ## Calculating the sum of the distances
        average = accumulated_distance/len(readings)  ## Calculating the average distance
        return average if average is not None else "No valid readings!!!!. Enter valid readings" ## Returning the average distance

    def print_message(message:str, number:float) -> str:
        """Formats a message with a number.

        Args:
            message (str): The message to be formatted.
            number (float): The number to be included in the message.

        Returns:
            str: The formatted message.
        """
        return f"{message} : {number:.2f} cm"
    
    ## Reading the sensor data from the file
    sensor_data_list = read_sensor_data(filename)
    
    ## Checking if the sensor data is empty
    if not sensor_data_list:
        print("No sensor data available.")
        return
    
    
    threshold = 35.00 ## Defining the threshold distance
    filter_above_35 = partial(threshold_filter, threshold) ## Creating a partial function with the threshold

    ## Processing the sensor data to convert the distance from inches to centimeters
    processed_readings = list(map(process_reading, sensor_data_list))
    filtered_sensor_readings = [record['distance'] for record in list(filter(filter_above_35, processed_readings))] ## Filtering the sensor data based on the threshold
    format_filtered = partial(print_message, "Filtered distance") ## Creating a partial function with the message
    
    ## Printing the filtered sensor readings
    print("Valid sensor readings(distances in cm):")
    ## Iterating over the filtered sensor readings and printing them
    for reading in filtered_sensor_readings:
        print(format_filtered(reading)) ## Printing the filtered sensor readings
        
    average = average_distance(filtered_sensor_readings) ## Calculating the average distance
    format_average = partial(print_message, "The Average distance of the filtered readings") ## Creating a partial function with the message
    
    ## Printing the average distance
    print(format_average(average))
    

