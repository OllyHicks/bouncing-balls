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
    
    ball_file = 'ball.png'
    
    def __init__(self, simulator, radius):
        # Basic properties
        self.simulator = simulator
        self.radius = radius
        self.mass = math.pi * radius**2
        
        # Image
        ball_image = pyglet.resource.image(self.ball_file)
        ball_image.anchor_x, ball_image.anchor_y = radius, radius
        ball_image.width = ball_image.height = radius*2
        
        pyglet.sprite.Sprite.__init__(self, ball_image, batch=self.simulator.batch)
        
        # Velocity
        self.vx = 300*random.random() - 150
        self.vy = 300*random.random() - 150
 
    def update(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        
        # Detect collision with walls
        
        if self.x - self.radius <= 0: # Left wall
            self.vx = self.vx * -1
        elif self.x + self.radius >= self.simulator.window.width: # Right wall
            self.vx = self.vx * -1
        
        if self.y - self.radius <= 0: # Bottom wall
            self.vy = self.vy * -1
        elif self.y + self.radius >= self.simulator.window.height: # Top wall
            self.vy = self.vy * -1
