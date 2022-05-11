
import re

s = "function4box"


if len(re.findall("function[\d]*box", s)) > 0:
    print("es")