class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return ("🍪" * self.cookies)

    def deposit(self, n):
        if n + self.cookies > self.capacity:
            raise ValueError
        self.cookies += n
        return self.cookies

    def withdraw(self, n):
        if self.cookies < n:
            raise ValueError
        self.cookies -= n
        return n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies
