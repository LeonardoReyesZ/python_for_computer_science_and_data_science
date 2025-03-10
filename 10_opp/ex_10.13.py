# ex_10.13.py
"""doctest"""

def maximum(value1, value2, value3):
    """Return the maximum of three values.

    >>> maximum(69, 23, 6)
    69
    >>> maximum(20, 199, 38)
    199
    >>> maximum(2, 45, 623)
    623

    >>> maximum(23.25, 22.34, 23.14)
    23.25
    >>> maximum(123.5, 23454.34, 4514.53)
    23454.34
    >>> maximum(123.34, 6234.34, 236434.633)
    236434.633

    >>> maximum('zebra', 'Zebra', 'ZEBRA')
    'zebra'
    >>> maximum('Zebra', 'zebra', 'ZEBRA')
    'zebra'
    >>> maximum('Zebra', 'ZEBRA', 'zebra')
    'zebra'

    """
    max_value = value1
    if max_value < value2:
        max_value = value2
    if max_value < value3:
        max_value = value3

    return max_value


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)