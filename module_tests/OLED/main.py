import oled

message = "OD1: x.xx            OD2: y.yy"

if oled.init():
  oled.write(message)