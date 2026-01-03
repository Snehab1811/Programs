import pytest
from unittest.mock import patch
from temperature_sensor import TemperatureSensor
import csv



#test for init

def tet_sensor_initialization_1():
    sensor=TemperatureSensor()
    assert sensor.min_temp == 20
    assert sensor.max_temp == 40

def test_sensor_initialization_2():
    sensor=TemperatureSensor(30,70)
    assert sensor.min_temp == 30
    assert sensor.max_temp == 70

#test for read_temperature(mocking because of random.choice(stubbing))

def test_read_temperature_within_range():
    sensor=TemperatureSensor(min_temp=20,max_temp=40)
    # using patch for random.choice
    with patch('random.choice',return_value=30):
        temp_1=sensor.read_temperature()
        assert temp_1 == 30

def test_read_temperature_min_10():
    sensor=TemperatureSensor(min_temp=20,max_temp=40)
    # using patch for random.choice for # min_temp - 10
    with patch('random.choice',return_value=10):
        temp_2=sensor.read_temperature()
        assert temp_2 == 10

def test_read_temperature_max_10():
    sensor=TemperatureSensor(min_temp=20,max_temp=40)
    # using patch for random.choice for # max_temp + 10
    with patch('random.choice',return_value=50):
        temp_3=sensor.read_temperature()
        assert temp_3 == 50

#trying to add Test case as csv file and parse tc from csv file
TC_List=[(10,"Low"),            # min_temp-10
    (20, "Low"),          # min_temp
    (25, "Meduim"),       # min_temp < temp <= max_temp - 10
    (30, "Meduim"),       # max_temp - 10 (30)
    (35, "Meduim"),       # max_temp - 5
    (40, "Meduim"),       # max_temp
    (50, "Very High"),    # max_temp + 10
    (41, "Very High"),    # Just above max_temp
    (19, "Low")]
def write_to_CSV_file():
    #crete csv file
    with open("tescase_csv.csv",w) as tescase_csv:
        #header for CSV file(TC)
        first_row=['mock_temp','expected_output']
        #write to csv file 
        csv_writter=csv.DictWriter(tescase_csv, fieldnames = first_row, delimiter=',')
        csv_writter.writeheader()

        for i in TC_List:
            csv_writter.writerow(i)


# Test cases for High_Low_temp
# I am using patch here to read_temperature() to control the return value

@pytest.mark.parametrize("mock_temp,expected_output",[ 
    (10,"Low"),            # min_temp-10
    (20, "Low"),          # min_temp
    (25, "Meduim"),       # min_temp < temp <= max_temp - 10
    (30, "Meduim"),       # max_temp - 10 (30)
    (35, "Meduim"),       # max_temp - 5
    (40, "Meduim"),       # max_temp
    (50, "Very High"),    # max_temp + 10
    (41, "Very High"),    # Just above max_temp
    (19, "Low"),          # Just below min_temp
])



def test_High_Low_temp_mock(mock_temp,expexted_output):
    sensor=TemperatureSensor(min_temp=20,max_temp=40)
#specified attribute of the sensor class(TemperatureSensor) read_temperature is replaced with a mock object
    with patch.object(sensor,'read_temperature',return_value=mock_temp):
        status= sensor.High_Low_temp()
        assert status == expexted_output
