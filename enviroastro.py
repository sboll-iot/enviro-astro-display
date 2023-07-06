# Copyright (c) 2023 Sascha Boll
# Author: Sascha Boll
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time
import sys
import ST7735
from PIL import Image, ImageDraw, ImageFont
import random

disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=4000000
)

WIDTH = disp.width
HEIGHT = disp.height
LED_RED = (238, 53, 41)
LED_YELLOW = (255, 241, 1)
LED_GREEN = (75, 175, 98)

disp.begin()

img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
draw = ImageDraw.Draw(img)


try:
    rect_colour = (0, 0, 0)
    draw.rectangle((0, 0, 160, 80), rect_colour)
    while True:
        for x in range(5):
            for y in range(10):
                next_led = random.randint(1, 3)

                if next_led == 1:
                    led_color = LED_RED
                elif next_led == 2:
                    led_color = LED_YELLOW
                else:
                    led_color = LED_GREEN
                draw.ellipse((16*y, 16*x, 16*(y+1), 16*(x+1)), outline=led_color, fill=led_color)
        disp.display(img)

except KeyboardInterrupt:
    sys.exit(0)        


