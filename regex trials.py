import re

import pathlib
import gzip

a = "salut 123, 3, 2, "

pattern=re.compile( r"\d{1,2}" ) # expected true

matches = pattern.finditer(a)

for thing in matches:
    print((thing).group(0))