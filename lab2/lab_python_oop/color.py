class Color:
    def __init__(self):
        self._color=None
    @property
    def col(self):
        return self._color

    @col.setter
    def col(self,val):
        self._color=val
