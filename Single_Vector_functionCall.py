import anki_vector
import time
import re
import string
import random
import threading
import multiprocessing as mp
from anki_vector.util import degrees, distance_mm, speed_mmps




# function to read the sensor data from proximity

def data_read():
    with anki_vector.Robot(name="Vector-T8B3") as robot:
        #with anki_vector.Robot(name="Vector-H3D8") as robot:   
        for i in range(400):
            time.sleep(0.1)
            proximity_data = robot.proximity.last_sensor_reading
            if proximity_data is not None:
                print('Proximity distance: {0}'.format(proximity_data.distance))
                measure = data_convert(format(proximity_data.distance))
                if(measure>300):
                    print("long")
                    break
                
def data_convert(str):
    """docstring for ():"""
    ans_str = re.findall(r"[-+]?\d*\.\d+|\d+", str)
    ans = [float(s) for s in ans_str]
    return ans[0]


def motion_control(robot_name):
    print("got it")
    with anki_vector.Robot(name=robot_name) as robot: 
        robot.behavior.drive_straight(distance_mm(500), speed_mmps(500))
        for i in range(10):
            print(i)
                
def main():
    data_read()
    name = "Vector-T8B3"
    motion_control(name)




if __name__=="__main__":
    main()     