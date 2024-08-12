class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.observers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            self._notify_observers()

    def _notify_observers(self):
        for observer in self.observers:
            observer.mark_for_update()
        for observer in self.observers:
            observer.update()

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self._value = None
        self.callbacks = []
        self.observers = []
        self._needs_update = True

        for input_cell in inputs:
            input_cell.observers.append(self)

        self.update()

    @property
    def value(self):
        self.update()
        return self._value

    def mark_for_update(self):
        self._needs_update = True
        for observer in self.observers:
            observer.mark_for_update()

    def update(self):
        if self._needs_update:
            old_value = self._value
            new_value = self.compute_function([input_cell.value for input_cell in self.inputs])
            self._needs_update = False
            if new_value != old_value:
                self._value = new_value
                self._run_callbacks()
                self._notify_observers()

    def _notify_observers(self):
        for observer in self.observers:
            observer.update()

    def _run_callbacks(self):
        for callback in self.callbacks:
            callback(self._value)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        while callback in self.callbacks:
            self.callbacks.remove(callback)