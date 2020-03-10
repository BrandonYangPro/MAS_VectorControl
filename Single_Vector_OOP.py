# This file we try to build the Vector class and realize the multi threading inside the class, making the functions implemented in parallel

import anki_vector
import time
import re
import string
import random
import threading
import multiprocessing as mp
from anki_vector.util import degrees, distance_mm, speed_mmps



class car:
    def __init__(self, name):
        self.name = name
    
    def drive_straight(self, vel, dist):
        
        with anki_vector.Robot(name=self.name) as robot: 
            robot.behavior.drive_straight(distance_mm(dist), speed_mmps(vel))
            #if(self.proximity_read()):
                #robot.behavior.drive_straight(distance_mm(dist), speed_mmps(vel/2))
    def print_a(self):
    
    def print_b(self):
        
    
    def proximity_read(self):
        with anki_vector.Robot(name=self.name) as robot:
            #with anki_vector.Robot(name="Vector-H3D8") as robot:   
            for i in range(20):
                time.sleep(0.2)
                proximity_data = robot.proximity.last_sensor_reading
                if proximity_data is not None:
                    # print('Proximity distance: {0}'.format(proximity_data.distance))
                    str = format(proximity_data.distance)
                    ans_str = re.findall(r"[-+]?\d*\.\d+|\d+", str)
                    ans = [float(s) for s in ans_str]
                    measure = ans[0]
                    
                    if(measure<100):
                        print("short")
                        return TRUE
                        
                        
