import time
import gc
import board
import displayio
import random
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon

# Constants
Turkey_CENTER_X = 110
Turkey_CENTER_Y = 100
Turkey_RADIUS = 50
Turkey_OFFSET = 7
STEM_OFFSET = 48
STEM_WIDTH = 12
STEM_HEIGHT = 24
MOON_X = 20
MOON_Y = 30
MOON_RADIUS = 10
CRESENT_OFFSET = 5
LIGHTNING = [(180, 0), (165, 40), (170, 40), (166, 60), (185, 30), (175, 30), (190, 0)]

# Colors
TURKEY= 0x000000
BACKGROUND = 0x22230A
MOON = 0x161616
STEM = 0x000000
WHITE = 0xFFFFFF


displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

dbus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(dbus, rotation=270, width=240, height=135, rowstart=40, colstart=53)


# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 3)
color_palette = displayio.Palette(5)
color_palette[0] = BACKGROUND
color_palette[1] = TURKEY
color_palette[2] = MOON
color_palette[3] = STEM
color_palette[4] = WHITE
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)
display.root_group = main_group

# Draw Turkey (Created from 3 circles and rectangle)
Turkey = []
for i in range(3):
    circle = Circle(Turkey_CENTER_X + ((i-1) * Turkey_OFFSET), Turkey_CENTER_Y, Turkey_RADIUS, fill=TURKEY)
    Turkey.append(circle)
for circles in Turkey:
    main_group.append(circles)
stem = Rect(Turkey_CENTER_X - int(STEM_WIDTH / 2), Turkey_CENTER_Y - STEM_OFFSET, STEM_WIDTH, STEM_HEIGHT, fill=STEM)
main_group.append(stem)



# Lightning
lightning = Polygon(LIGHTNING, outline=BACKGROUND, close=True, colors=2)
main_group.append(lightning)

count = 0
direction = 1
while True:
    pass
