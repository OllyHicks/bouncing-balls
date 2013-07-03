#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Olly Hicks <me@ollyhicks.co.uk>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import math
import random

import subprocess
import tempfile
 
import pyglet
from simulator import *

import sys
import argparse

def main(fullscreen = True, image_directory=None, num_balls=None, max_radius=None):
    screenshot = None
    
    if fullscreen:
        screenshot = get_screenshot()
        window = pyglet.window.Window(fullscreen=True)
        window.set_mouse_visible(False)
    else:
        window = pyglet.window.Window(visible=False, caption="Collision")
        
    sim = Simulator(window, image_directory, num_balls, max_radius)
    
    # clear the window and draw the scene
    @window.event
    def on_draw():
        window.clear()
        if not screenshot == None:
            screenshot.blit(0, 0)
        sim.batch.draw()
    
    if fullscreen:
        @window.event
        def on_key_press(symbol, modifiers):
            pyglet.app.exit()
        
        @window.event
        def on_mouse_motion(x, y, dx, dy):
            pyglet.app.exit()
            
        def on_mouse_press(x, y, button, modifiers):
            pyglet.app.exit()
    
    # schedule the update function, 60 times per second
    pyglet.clock.schedule_interval(sim.update, 1.0/60.0)
    
    # clear and flip the window, otherwise we see junk in the buffer before the first frame
    window.clear()
    window.flip()
     
    # make the window visible at last
    window.set_visible(True)
     
    # finally, run the application
    pyglet.app.run()
    
    return 0

def get_screenshot():
    handle, path = tempfile.mkstemp('.png')
    subprocess.call(['import', '-window',  'root', path])
    return pyglet.image.load(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulate the elastic collision of balls.')
    
    parser.add_argument('--windowed', action='store_true', default=False,
                       help='Run the simulation in a window rather than fullscreen')
                       
    parser.add_argument('--images', type=str, default='balls',
                       help='Directory of the images for the balls')
                       
    parser.add_argument('--num_balls', type=int, default=40,
                       help='Directory of the images for the balls')
                       
    parser.add_argument('--max_radius', type=int, default=50,
                       help='Maximum radius of the balls')

    args = parser.parse_args()
    
    main(not args.windowed, args.images, args.num_balls, args.max_radius)
