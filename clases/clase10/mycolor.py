"""
color.py

The color module defines the Color class and some popular Color
objects.
Modified from https://introcs.cs.princeton.edu/python/code/color.py.html
"""

class Color:
    """
    A Color object models an RGB color.
    """
    def __init__(self, r=0, g=0, b=0):
        """
        Construct self such that it has the given red (r),
        green (g), and blue (b) components.
        """
        self._r = r  # Red component
        self._g = g  # Green component
        self._b = b  # Blue component
    
    def red(self):
        """
        Return the red component of self.
        """
        return self._r
    
    def green(self):
        """
        Return the green component of self.
        """
        return self._g
    
    def blue(self):
        """
        Return the blue component of self.
        """
        return self._b
    
    def __str__(self):
        """
        Return the string equivalent of self, that is, a
        string of the form '(r, g, b)'.
        """
        return '(' + str(self._r) + ', ' + str(self._g) + ', ' + \
            str(self._b) + ')'

def _main():
    """
    For testing:
    """
    
    c1 = Color(128, 128, 128)
    print(c1)
    print(c1.red())
    print(c1.green())
    print(c1.blue())

if __name__ == '__main__':
    _main()
