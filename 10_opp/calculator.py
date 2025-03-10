# calculator.py
"""Calculator class"""

class Calculator:

    def __init__(self, num1=0, num2=0):
        self._num1 = num1
        self._num2 = num2

    @property
    def sum(self):
        return self._num1 + self._num2

    @property
    def difference(self):
        return self._num1 - self._num2

    @property
    def product(self):
        return self._num1 * self._num2

    @property
    def division(self):
        if self._num2 != 0:
            return self._num1 / self._num2

        return "Division by zero is undefined"
