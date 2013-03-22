#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ball.py
#  
#  Copyright 2013 Olly Hicks <olly@olly-laptop>
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
 
import pyglet
from pyglet.gl import *


class Ball(pyglet.sprite.Sprite):
    
    colours = ('red', 'green', 'blue', 'sky', 'yellow', 'purple', 'orange', 'pink')
    
    def __init__(self, simulator, radius, x=None, y=None):
		# Basic properties
        self.simulator = simulator
        self.radius = radius
        self.mass = math.pi * radius**2
        
        # Colour
        self.colour = random.choice(self.colours)
        
        # Image
        ball_image = pyglet.resource.image(self.colour+'.png')
        ball_image.anchor_x = ball_image.anchor_y = ball_image.width * 0.5
		
		# Init sprite
        pyglet.sprite.Sprite.__init__(self, ball_image, batch=self.simulator.batch)
        
        # Scale image
        self.scale = 2*self.radius / (ball_image.width * 1.0)
        
        # Velocity
        self.vx = 300*random.random() - 150
        self.vy = 300*random.random() - 150
        
        # Position
        if not x == None:
			self.x = x
        if not y == None:
			self.y = y
 
    def update(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        
        # Detect collision with walls
        
        if self.x - self.radius <= 0: # Left wall
            self.vx = self.vx * -1
            self.x = self.radius
        elif self.x + self.radius >= self.simulator.window.width: # Right wall
            self.vx = self.vx * -1
            self.x = self.simulator.window.width - self.radius
        
        if self.y - self.radius <= 0: # Bottom wall
            self.vy = self.vy * -1
            self.y = self.radius
        elif self.y + self.radius >= self.simulator.window.height: # Top wall
            self.vy = self.vy * -1
            self.y = self.simulator.window.height - self.radius
