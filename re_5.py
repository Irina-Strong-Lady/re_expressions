import re

text = "<font color=#CC0000 bg=#ffffff>"
#match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
#match = match.group(0, 1, 2)
#match = match.groups()
#match = match.lastindex
#match = match.start(1)
#match = match.end(2)
#match = match.span(2)
#match = match.endpos
#match = match.pos
#match = match.re
#match = match.string

#match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)


#match = match.groupdict()
#match = match.lastgroup
#match = match.expand(r"\g<key>:\g<value>")

#print(match)

# for match in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
#     print(match)

# for match in re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
#     print(match)

match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)


