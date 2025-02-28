import csv 
from functools import reduce,partial

def read_sensor_data(filename : str) -> list[dict]:
    try:
        with open(filename,'r') as data_file:
            sensor_data_list = []
            sensor_data = csv.reader(data_file)
            header = next(sensor_data)
            # print(header)
            
            for record in sensor_data:
                sensor_data_list.append({
                    header[0] : int(record[0]),
                    header[1] : float(record[1]),
                    header[2] : record[2]
                })
            return sensor_data_list
    except FileNotFoundError:
        print("Pass a Valid filename!!!!")
    
def inches_to_cm(inches : float) -> float:
    return inches * 2.54

def process_reading(reading:dict) -> dict:
    reading_copy = reading.copy()
    reading_copy['distance'] = inches_to_cm(reading_copy['distance'])
    return reading_copy

def threshold_filter(threshold : float, reading:dict ) -> bool:
    return reading['distance'] >= threshold



def average_distance(readings : list):
    accumulated_distance = reduce(lambda x,y : x+y, readings)
    average = accumulated_distance/len(readings)
    
    return average if average is not None else "No valid readings!!!!. Enter valid readings"




path_data = r'../config/sensor_data.csv'
sensor_data_list = read_sensor_data(path_data)

print(f" Before : {sensor_data_list[0]}")
print(process_reading(sensor_data_list[0]))
print(f" After : {sensor_data_list[0]}")

processed_readings = list(map(process_reading, sensor_data_list))
# print(list(processed_readings))
filtered_sensor_readings = [record['distance'] for record in list(filter(filter_above_20, processed_readings))]

# print(filtered_sensor_readings)
average = average_distance(filtered_sensor_readings)

print(average)

