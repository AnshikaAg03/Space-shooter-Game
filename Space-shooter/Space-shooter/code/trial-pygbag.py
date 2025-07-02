from pyray import *
import time

# Enable more verbose logging
import os
os.environ['RAYLIB_LOG_LEVEL'] = '4'  # Debug level

init_audio_device()

print("Loading sound with debug info...")
laser_sound = load_sound("audio/laser_stereo.ogg")

# Check if we get the same warnings as in search results
print("Playing sound...")
play_sound(laser_sound)
time.sleep(3)

unload_sound(laser_sound)
close_audio_device()
