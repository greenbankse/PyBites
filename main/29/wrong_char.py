def get_index_different_char(chars):
    loc = [indx for indx, s in enumerate(chars) if not str(s).isalnum()]
    # if len(loc) == 1:
    #     return loc[0]
    # else:
    #     return [indx for indx, s in enumerate(chars) if str(s).isalnum()][0]
    return (
        loc[0] if len(loc) == 1 else [indx for indx, s in enumerate(chars) if str(s).isalnum()][0]
    )


# s = ["d", "g", "3", ".", "g"]
# print(s)
# print([indx for indx, s in enumerate(s) if not s.isalnum()][0])

s = ["A", "f", ".", "Q", 2]
print(get_index_different_char(s))
