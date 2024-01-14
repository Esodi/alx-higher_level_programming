#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        # Create a valid Rectangle instance
        rect = Rectangle(10, 5, 2, 3, id=1)

        # Try to set invalid values to provoke exceptions
        rect.width = "invalid"
    except TypeError as te:
        print(f"Caught TypeError: {te}")

    try:
        # Try to set a negative value to provoke ValueError
        rect.height = -5
    except ValueError as ve:
        print(f"Caught ValueError: {ve}")
