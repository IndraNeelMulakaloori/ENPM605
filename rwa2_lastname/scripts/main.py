## Importing the function process_sensor_pipeline from sensor_pipeline.py
from sensor_pipeline import process_sensor_pipeline


if __name__ == '__main__':
    ## Calling the function process_sensor_pipeline
    ## with the path to the sensor data file
    ## as the argument
    path_data = r'../config/sensor_data.csv'
    process_sensor_pipeline(path_data)