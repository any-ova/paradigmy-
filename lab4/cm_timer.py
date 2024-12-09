from contextlib import contextmanager
import time


class cm_timer_1:

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *_):
        self.finish = time.time()
        self.work_time = self.finish - self.start
        print(self.work_time)


@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        finish = time.time()
        work_time = finish - start
        print(work_time)


if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(3)

    with cm_timer_2():
        time.sleep(3)
