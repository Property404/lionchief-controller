from lc import LionChief
import time

# Replace this mac address with the one
# belonging to your train
chief = LionChief("44:A6:E5:41:AE:72")
chief.set_bell_pitch(1)

# Gracefully start or stop
def ramp(start_speed, end_speed):
    speed = start_speed
    while speed != end_speed:
        chief.set_speed(speed)
        if speed > end_speed:
            speed -= 1
        else:
            speed += 1
        time.sleep(.2)
    chief.set_speed(end_speed)

while True:
    # Let the conductor say something
    chief.speak()
    # Have to give adequate to speak, otherwise horn
    # will cut off the conductor's voice
    time.sleep(3.5)

    # Time to go
    chief.set_horn(True)
    ramp(0, 6)

    # Turn the horn off
    time.sleep(2)
    chief.set_horn(False)

    # Keep training along
    time.sleep(10)

    # Reverse 
    ramp(6,0)
    chief.set_reverse(True)
    ramp(0,6)
    time.sleep(10)

    # Back to normal
    ramp(6,0)
    chief.set_reverse(False)
    ramp(0,6)
    time.sleep(40)

    # This is our stop
    chief.set_bell(True)
    time.sleep(1)
    ramp(6,0)
    time.sleep(1)
    chief.set_bell(False)
    time.sleep(180)

