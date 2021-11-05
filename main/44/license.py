from random import randint

selection = "abcdefghijklmnopqrstuvwxyz0123456789".upper()


def gen_key(*, parts=4, chars_per_part=8):
    string0 = "-".join(
        [
            "".join([selection[randint(a=0, b=len(selection) - 1)] for i in range(chars_per_part)])
            for j in range(parts)
        ]
    )
    return string0
