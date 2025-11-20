"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
EACH_LAYER_PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return 0 if elapsed_bake_time > EXPECTED_BAKE_TIME else EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time to make layers

        :param number_of_layers: int - how many layers that you made
        :return: int - total times that have been taken to make layers

        Function that takes the total layers that been made and calculates total time it took to prepare
    """
    return number_of_layers * EACH_LAYER_PREPARATION_TIME

def elapsed_time_in_minutes(layers, elapsed_time):
    """Calculate the total elapsed time in minutes

    :param layers: int - how many layers that you made
    :param elapsed_time: int - current elapsed time
    :return: int - total making time that have been elapsed

    Function that takes the total layers that been made and current elapsed time then calculates total elapsed time
    """
    return preparation_time_in_minutes(layers) + elapsed_time



