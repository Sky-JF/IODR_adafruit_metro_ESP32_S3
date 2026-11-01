python -m mpy_cross -o build/main.mpy main.py

python -m mpy_cross -o build/lib/config_routine.mpy lib/config_routine.py
python -m mpy_cross -o build/lib/influxdb_lib.mpy lib/influxdb_lib.py
python -m mpy_cross -o build/lib/led_ctrl.mpy lib/led_ctrl.py
python -m mpy_cross -o build/lib/oled.mpy lib/oled.py
python -m mpy_cross -o build/lib/sensors.mpy lib/sensors.py
python -m mpy_cross -o build/lib/wifi.mpy lib/wifi.py
python -m mpy_cross -o build/lib/manual_config.mpy lib/manual_config.py
python -m mpy_cross -o build/lib/secrets.mpy lib/secrets.py
