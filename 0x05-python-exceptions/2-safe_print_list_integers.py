def safe_print_list_integers(my_list=[], x=0):

    """Print the first x elements of a list that are integers.


    Args:

        my_list (list): The listt to print elements from.

        x (int): Thhe number of elements of my_list to print.


    Returns:

        The numbeer of elements printed.

    """

    ret = 0

    for i in range(0, x):

        try:

            print("{:d}".format(my_list[i]), end="")

            ret += 1

        except (ValueError, TypeError):

            continue

    print("")

    return (ret)
