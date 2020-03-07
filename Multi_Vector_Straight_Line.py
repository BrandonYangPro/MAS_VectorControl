# This code provides that the cars/vectors would 

import anki_vector
import time
import re
import string
import random
import threading
import multiprocessing as mp
from anki_vector.util import degrees, distance_mm, speed_mmps




def motion_control(robot_name, dist, vel):
    with anki_vector.Robot(name=robot_name) as robot:
        while True:
            robot.behavior.drive_straight(distance_mm(dist), speed_mmps(vel))
            proximity_data = robot.proximity.last_sensor_reading
            if proximity_data is not None:
                print('Proximity distance: {0}'.format(proximity_data.distance))
                measure = data_convert(format(proximity_data.distance))
                if(proximity_read(robot_name)):
                    robot.behavior.drive_straight(distance_mm(dist), speed_mmps(vel/5))        
        
def proximity_read(robot_name):
    with anki_vector.Robot(name=robot_name) as robot:
            #with anki_vector.Robot(name="Vector-H3D8") as robot:   
        for i in range(20):
            time.sleep(0.1)
            proximity_data = robot.proximity.last_sensor_reading
            if proximity_data is not None:
                str = format(proximity_data.distance)
                ans_str = re.findall(r"[-+]?\d*\.\d+|\d+", str)
                ans = [float(s) for s in ans_str]
                measure = ans[0]
                    
                if(measure<100):
                    print("short")
                    return True


def data_convert(str):
    """docstring for ():"""
    ans_str = re.findall(r"[-+]?\d*\.\d+|\d+", str)
    ans = [float(s) for s in ans_str]
    return ans[0]
    
    

    
def main():
    robot_team = ["Vector-T8B3", "Vector-H3D8"]
    dist = 500
    vel = 500
    T1 = threading.Thread(target=motion_control, args=(robot_team[0],dist,vel,))
    T2 = threading.Thread(target=motion_control, args=(robot_team[1],dist,vel,))
    T1.start()
    T2.start()
    
if __name__=="__main__":
    main()    
        
                





# define the vector class

        
# plot the trajectory


# car following model implementation here

"""
IDM:

dV = velocity_current()-velocity_pre()
dX = distance_read()
s_t = s0+v*T+v*dV/2/np.sqrt(a*b)
Acc = a*(1-(va/vt)-(s_t/s_a)**2)

""" 

