#!/user/bin/python3
"""
Amenity class inherited from BaseModel class module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherited from BaseModel class
    Attribute:
            name (str): amenity or address name of the place
    """
    name = ""
