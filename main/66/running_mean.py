import numpy as np


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    return [np.round(np.mean(sequence[:n]), 2) for n in range(1, len(sequence) + 1)]


print(running_mean([]))
