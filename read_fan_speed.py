import RPi.GPIO as GPIO
import time

# pin config
RPM_PIN = 14
RPM_PULSE = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RPM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

t = time.time()
rpm = 0

def get_rpm(n):
    global t
    global rpm

    dt = time.time() - t
    # reject spuriously short pulses
    if dt < 0.005:
        return  

    freq = 1 / dt
    rpm = (freq / RPM_PULSE) * 60
    t = time.time()

GPIO.add_event_detect(RPM_PIN, GPIO.FALLING, get_rpm)

try:
    while True:
        print("%.f RPM" % rpm)
        rpm = 0
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()