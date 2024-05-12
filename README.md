<h1>Setup</h1>

Model: Raspberry Pi 3B+\
Fan: Noctua NF-A4x10 5V PWM

- yellow = 5V  --> 5V
- black  = ground --> Ground
- green  = RPM --> GPIO 14 (UART TX)
- blue   = PWM Signal --> GPIO 18 (PWM)

<h1>Instruction</h1>

```diff
# setup service unit file
sudo cp pifancontrol.service /etc/systemd/system/pifancontrol.service

# start service
sudo systemctl start pifancontrol

# ensure service starts on boot:
sudo systemctl enable pifancontrol

# check service status
sudo systemctl status pifancontrol
```