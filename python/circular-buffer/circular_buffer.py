class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return data

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size == self.capacity:
            self.buffer[self.start] = data
            self.start = (self.start + 1) % self.capacity
            self.end = (self.end + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.start = 0
        self.end = 0
        self.size = 0
