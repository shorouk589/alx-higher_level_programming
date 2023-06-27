#!/usr/bin/python3


import sys



def safe_function(fct, *args):

    """Executes a functionn safely.


    Args:

        fct: The functionn to execute.

        args: Arguments .


    Returns:

        If an error occurs - None.

        Otherwise - thhe result of the call to fct.

    """

    try:

        result = fct(*args)

        return (result)

    except:

        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (None)
