import re

#take a string and return list of the words in the string; exclude numbers only
def words(string_in):
    match = re.findall(r"\d*\S*[A-Za-z]\w+", string_in)
    if match == []:
        return None
    else:
        return match

def phone_number(num_string):
    match = re.search(r"\(?(\d{3})\)?[-.]?\s*(\d{3})[\-\.]?(\d{4})", num_string)
    if match == None:
        return None
    else:
        cleaned = "{}-{}-{}".format(*match.groups())
        return {"area_code": cleaned[0:3], "number": cleaned[4:12]}
