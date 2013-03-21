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
    def __init__(self, simulator, radius):
        self.simulator = simulator
        self.radius = radius
        self.mass = math.pi * radius**2
        
        pattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
 
        image = pyglet.image.create(radius*2, radius*2, pattern)
        image.anchor_x, image.anchor_y = radius, radius
 
        pyglet.sprite.Sprite.__init__(self, image, batch=self.simulator.batch)
 
        # reset ourselves
        self.reset()
 
    def reset(self):
        # place ourselves in the centre of the playing field
        self.x, self.y = 400, 250
 
        # give ourselves a random direction within 45 degrees of either paddle
        angle = random.random()*math.pi*2
        # convert that direction into a velocity
        self.vx, self.vy = math.cos(angle)*300, math.sin(angle)*300
    
    def update(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
