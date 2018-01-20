import random


def pickRandom(sequence):
    if isinstance(sequence, list):
        for i, e in enumerate(sequence):
            if random.random() < 1.0 / (i + 1):
                result = e
    elif isinstance(sequence, dict):
        for i, e in enumerate(sequence.itervalues()):
            if random.random() < 1.0 / (i + 1):
                result = e
    else:
        result = sequence[0]
    return result
