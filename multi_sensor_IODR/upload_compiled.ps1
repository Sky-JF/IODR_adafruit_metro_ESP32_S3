mpremote.exe fs cp ./build/launcher_main.py :main.py
mpremote.exe fs cp ./build/main.mpy :app.mpy
mpremote.exe fs cp ./build/lib/sensors.mpy :/lib/
mpremote.exe fs cp ./build/lib/config_routine.mpy :/lib/
mpremote.exe fs cp ./build/lib/influxdb_lib.mpy :/lib/
mpremote.exe fs cp ./build/lib/wifi.mpy :/lib/
mpremote.exe fs cp ./build/lib/secrets.mpy :/lib/
mpremote.exe fs cp ./build/lib/led_ctrl.mpy :/lib/
mpremote.exe fs cp ./build/lib/manual_config.mpy :/lib/
mpremote.exe fs cp ./build/lib/oled.mpy :/lib/
#mpremote.exe mip install github:sparkfun/qwiic_as726x_py
#mpremote.exe mip install github:sparkfun/qwiic_veml6030_py
#mpremote.exe mip install github:sparkfun/qwiic_tca9548a_py
#mpremote.exe mip install github:sparkfun/qwiic_oled_base_py
