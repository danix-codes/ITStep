# import os
# import colorama
# import random
#
# colorama.init(autoreset=True)
#
# barvy = [
#     colorama.Fore.BLUE, \
#     colorama.Fore.YELLOW, \
#     colorama.Fore.RED, \
#     colorama.Fore.WHITE, \
#     colorama.Fore.MAGENTA
# ]
#
# for i in range(10):
#     line = ""
#     for j in range(40):
#         line += random.choice(barvy) + "█"
#     print(line)

import os
import colorama
import random

colorama.init(autoreset=True)

barvy = [
    colorama.Fore.BLUE,
    colorama.Fore.YELLOW,
    colorama.Fore.RED,
    colorama.Fore.WHITE,
    colorama.Fore.MAGENTA
]

for i in range(10):
    line = ""
    for j in range(10):
        if j == i or j == (9 - i):
            line += colorama.Fore.GREEN + "█"
        else:
            line += colorama.Fore.WHITE + "█"
    print(line)
