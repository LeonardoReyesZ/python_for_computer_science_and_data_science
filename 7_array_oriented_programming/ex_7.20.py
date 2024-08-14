# ex_7.20: performance analisys
import numpy as np
import random
import timeit

values = [1, 10, 100, 1000, 10000, 100000, 1000000]

print( f"{'Number of values':<20}{'List average execution time':<30}"
       f"{'array average execution time':<30}" )

for value in values:
    # Time list comprehension using timeit.timeit
    list_time = timeit.timeit(
        stmt = f"[random.randrange(1,7) for i in range({value})]",
        setup = f"import random", # this runs once before the timing begins
        number = 1000 # times to execute
    )

    # Time np.random.randint using timeit.timeit
    array_time = timeit.timeit(
        stmt = f"np.random.randint(1,7,{value})",
        setup = "import numpy as np", # this runs once before the timing begins
        number = 100 # times to execute
    )

    print( f"{value:<20}{f'{list_time:.4f}(ms)':<30}{f'{array_time:.4f}(ms)':<30}" )

