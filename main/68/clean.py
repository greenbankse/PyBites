def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    from string import punctuation

    return "".join([s for s in input_string if s not in punctuation])


print(remove_punctuation("fsdkafbhjkadf./l,faksdfjakdf?"))

from string import punctuation

print(punctuation.count("fsdkafbhjkadf./l,faksdfjakdf?"))
# punctuation.

