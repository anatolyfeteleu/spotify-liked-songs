import functools
import sys

from settings import LOGS_ENABLED

FILLER = '\n' + '-' * 64 + '\n'


class Beautify:

    def __init__(self, func):

        functools.update_wrapper(self, func)

        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):

        self.calls += 1

        # Header
        if LOGS_ENABLED:

            header = f'{self.func.__name__}'
            if self.calls > 1:
                header = header + f'({self.calls})'

            sys.stdout.write(FILLER)
            sys.stdout.write(f'|{header:^62}|')
            sys.stdout.write(FILLER)

        result = self.func(*args, **kwargs)

        # Footer
        if LOGS_ENABLED:
            sys.stdout.write('DONE')
            sys.stdout.write('\n')

        return result

    def __get__(self, obj, objtype):
        """Implement 'get' descriptor"""

        return functools.partial(self.__call__, obj)
