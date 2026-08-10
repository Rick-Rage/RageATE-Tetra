from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units
from zaber_motion.ascii import AlertEvent
from zaber_motion.ascii import AllAxes
from zaber_motion.ascii import Lockstep
from zaber_motion.ascii import Axis

Library.enable_device_db_store()

def move(axis,amu):
    # ax.move_relative(amu,Units.LENGTH_MILLIMETRES)
    axis.move_absolute(amu, Units.NATIVE)

def sel_ant (ax,ay,az,port):

    x_loc = float(ax)
    y_loc = float(ay)
    z_loc = float(az)

    with Connection.open_serial_port(port) as connection:
        device_list = connection.detect_devices()
        print(device_list)
        print("Found {} devices".format(len(device_list)))
        # Declare device's and axes
        MCC3 = device_list[0] # X-MCC3 controller is the first device on device_list for me. In Pyhon, lists start their index at 0.
        y_1 = MCC3.get_axis(1)
        y_2 = MCC3.get_axis(2)
        x = MCC3.get_axis(3)
        z = MCC3.get_axis(4)
        lockstep = MCC3.get_lockstep(1)  # Make lockstep group 1 for X-MCC2

        speed_x = x.settings.get("maxspeed", Units.VELOCITY_MILLIMETRES_PER_SECOND)
        speed_z = z.settings.get("maxspeed", Units.VELOCITY_MILLIMETRES_PER_SECOND)
        speed_y1 = y_1.settings.get("maxspeed", Units.VELOCITY_MILLIMETRES_PER_SECOND)
        speed_y2 = y_2.settings.get("maxspeed", Units.VELOCITY_MILLIMETRES_PER_SECOND)

        x.settings.set("maxspeed",310,Units.VELOCITY_MILLIMETRES_PER_SECOND)
        y_1.settings.set("maxspeed",310,Units.VELOCITY_MILLIMETRES_PER_SECOND)
        z.settings.set("maxspeed",63,Units.VELOCITY_MILLIMETRES_PER_SECOND)
        y_2.settings.set("maxspeed",310,Units.VELOCITY_MILLIMETRES_PER_SECOND)

        if not lockstep.is_enabled():
            lockstep.enable(1, 2) # Enable lockstep on axis 1 and 2

        move(x,y_loc)
        move(z,z_loc)
        move(lockstep,x_loc)

def read(port):
    with Connection.open_serial_port(port) as connection:
        device_list = connection.detect_devices()
        # Declare device's and axes
        MCC3 = device_list[0] # X-MCC3 controller is the first device on device_list for me. In Pyhon, lists start their index at 0.
        y_1 = MCC3.get_axis(1)
        y_2 = MCC3.get_axis(2)
        x = MCC3.get_axis(3)
        z = MCC3.get_axis(4)
        cord_y = str(y_1.get_position())
        cord_x = str(x.get_position())
        cord_z = str(z.get_position())
        cords = [cord_x,cord_y,cord_z]
        return cords
