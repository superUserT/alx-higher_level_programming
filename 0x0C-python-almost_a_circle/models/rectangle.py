#!/usr/bin/python3
"""A base Class for the model Rectangle"""
from models.base import Base

class Rectangle(Base):
    """Represents the base model"""


    def __init__(self, width, height, x=0, y=0, id=None): 
        """Initialize a new Base"""
        super().__init__(id)
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        