import anki_vector
import time
import re
import string
import random
import threading
import multiprocessing as mp
from anki_vector.util import degrees, distance_mm, speed_mmps




# two robot names:   Vector-T8B3     &&     Vector-H3D8


def motion_control(robot_name):
    print("got it")
    with anki_vector.Robot(name = robot_name) as robot: 
        print("start")
        robot.behavior.drive_straight(distance_mm(500), speed_mmps(500))



def main():
    robot_team = ["Vector-T8B3", "Vector-H3D8"]
    T1 = threading.Thread(target=motion_control, args=(robot_team[0],))
    T2 = threading.Thread(target=motion_control, args=(robot_team[1],))
    T1.start()
    T2.start()
    
if __name__=="__main__":
    main()    
        
 
