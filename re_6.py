import re

# text = "+7(909)452-73-11"
# match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
# print(match)


# text = """<point lon="40.8482" lat="52.6274" />
# <point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
# <point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
# """
#
# arr = re.split(r"[\n;,]+", text)
# print(arr)


# text = """Москва
# Казань
# Тверь
# Самара
# Уфа"""
#
# list = re.sub(r"\s*(\w+)\s*", r"<option>\1<option>\n", text)
# print(list)


# text = """Москва
# Казань
# Тверь
# Самара
# Уфа"""
#
# count = 0
# def replFind(match): # Match
#     global count
#     count += 1
#     return f"<option value='{count}'>{match.group(1)}</option>\n"
#
# list = re.sub(r"\s*(\w+)\s*", replFind, text)
# print(list)


# text = """Москва
# Казань
# Тверь
# Самара
# Уфа"""
#
# list, total = re.subn(r"\s*(\w+)\s*", r"<option>\1<option>\n", text)
# print(list, total)


text = """Москва
Казань
Тверь
Самара
Уфа"""

count = 0
def replFind(match):
    global count
    count += 1
    return f"<option value='{count}'>{match.group(1)}</option>\n"

rx = re.compile(r"\s*(\w+)\s*")
list, total = rx.subn(r"<option>\1</option>\n", text)
list2 = rx.sub(replFind, text)
print(list, total, list2, sep="\n")


