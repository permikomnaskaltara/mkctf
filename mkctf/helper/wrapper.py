# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     file: wrapper.py
#     date: 2018-03-01
#   author: paul.dautry
#  purpose:
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# =============================================================================
#  IMPORTS
# =============================================================================
from functools import wraps
# =============================================================================
#  FUNCTIONS
# =============================================================================
def lazy():
    """Wraps a class method with this function to turn it into a lazy getter.

    Class member value will be computed on the first call to this
    function and will never be computed again after that.

    Decorators:
        wraps
    """
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *args, **kwds):
            member = '__{}'.format(f.__name__)
            if not hasattr(self, member):
                setattr(self, member, f(self, *args, **kwds))

            return getattr(self, member)

        return wrapped

    return wrapper
