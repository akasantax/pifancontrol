import RPi.GPIO as GPIO
import time
import subprocess

# pin config
PWM_PIN = 18
PWM_FREQ = 100

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PWM_PIN,GPIO.OUT)
fan = GPIO.PWM(PWM_PIN,PWM_FREQ)
fan.start(0)

def get_temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not get temperature')

print("fan control running...")

try:
    while True:
        temp = get_temp()
        if temp > 70:
            fan.ChangeDutyCycle(100)
        elif temp > 60:
            fan.ChangeDutyCycle(70)
        else:
            fan.ChangeDutyCycle(50)
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()