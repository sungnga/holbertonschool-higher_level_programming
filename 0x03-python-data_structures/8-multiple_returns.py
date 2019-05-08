#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = (len(sentence), sentence[0])
    if not sentence:
        sentence[0] = None
        return (tuple[0], tuple[1])
    return (tuple[0], tuple[1])
