## GPIO test

# import pin controller
from periphery import GPIO

# Open GPIO 6 with output direction
gpio_out = GPIO(6, "out")

gpio_out.write(True)

gpio_out.close()