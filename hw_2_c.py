import time
import random
import functools

def timeout(rps):
    def decorator(foo):
        @functools.wraps(foo)
        def wrapper(*arsg, **kwargs):
            t_start = time.time()
            result = foo(*arsg, **kwargs)
            t_delta = time.time() - t_start
            sleep = (1 / rps) - t_delta if ((1 / rps) - t_delta) > 0 else 0
            time.sleep(sleep)
            return result
        return wrapper
    return decorator

# @timeout(rps=5)
# def func():
#     pass

# if __name__ == "__main__":
#     t_start = time.time()
#     for i in range(10):
#         func()
#     t_delta = time.time() - t_start
#     print("{:.2f}".format(t_delta))

# @timeout(rps=5)
# def func():
#     time.sleep(random.random() * 0.1)

# if __name__ == "__main__":
#     t_start = time.time()
#     for i in range(10):
#         func()
#     t_delta = time.time() - t_start
#     print("{:.2f}".format(t_delta))

# @timeout(rps=5)
# def func():
#     time.sleep(0.3)

# if __name__ == "__main__":
#     t_start = time.time()
#     for i in range(10):
#         func()
#     t_delta = time.time() - t_start
#     print("{:.2f}".format(t_delta))