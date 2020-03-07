import anki_vector
import time
import re
import string
import random
import threading
import multiprocessing as mp
from anki_vector.util import degrees, distance_mm, speed_mmps





def motion_control(robot_name):
    print("got it")
    with anki_vector.Robot(name=robot_name) as robot: 
        robot.behavior.drive_straight(distance_mm(500), speed_mmps(500))
        for i in range(10):
            print(i)

# two robot names:   Vector-T8B3     &&     Vector-H3D8

# version 1 on parallel processing
'''
def main():
    T1 = mp.Process(target=motion_control("Vector-T8B3"))
    T2 = mp.Process(target=motion_control("Vector-H3D8"))
    T1.start()
    T2.start()
'''

# version 2 on parallel processing
'''
def main():
    pool = mp.Pool(processes = 2)
    robot_team = ["Vector-T8B3", "Vector-H3D8"]
    results = [pool.apply(motion_control, args = (x,)) for x in robot_team]
'''



# version 3 on parallel processing by using threading.Thread



def main():
    robot_team = ["Vector-T8B3", "Vector-H3D8"]
    T1 = threading.Thread(target=motion_control, args=(robot_team[0],))
    T2 = threading.Thread(target=motion_control, args=(robot_team[1],))
    T1.start()
    T2.start()


if __name__ == "__main__":
    main()