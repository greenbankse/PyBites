INDENTS = 4

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

# def print_hanging_indents(poem):
#     poem = [line.strip() for line in poem.split('\n')]
#     indent = False
#     for line in poem:
#         if line == '':
#             indent = False
#             continue
#         print(line) if (line!='') and not indent else print('    '+line)
#         indent = True

def print_hanging_indents(poem):
    """You can use textwrap's fill but this worked better for us"""
    for part in poem.split("\n\n"):
        lines = [line.strip() for line in part.splitlines()
                 if line.strip()]
        print(lines[0])
        for line in lines[1:]:
            print(' ' * INDENTS + line)

print(shakespeare_unformatted)
print_hanging_indents(shakespeare_unformatted)