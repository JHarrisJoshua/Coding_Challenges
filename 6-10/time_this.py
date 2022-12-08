import functools
import time


def time_this(func):
    """
    The function times how many seconds it takes for the function to run.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Calls the function and records time needed to complete."""
        begin_time = time.perf_counter()
        func(*args, **kwargs)
        elapsed_time = time.perf_counter() - begin_time
        return elapsed_time
    return wrapper
