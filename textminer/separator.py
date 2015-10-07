import re

def words(string_in):
    match = re.findall(r"\w*\-*[A-Za-z]\w*", string_in)
    if match == []:
        return None
    else:
        return match

def phone_number(num_string):
    match = re.search(r"\(?(\d{3})\)?[\-\.]?\s*(\d{3})[\-\.]?(\d{4})", num_string)
    if match:
        cleaned = "{}-{}-{}".format(*match.groups())
        return {"area_code": cleaned[0:3], "number": cleaned[4:12]}

def money(mon_string):
    match = re.search(r"^\$([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(.[0-9]{2})?$", mon_string)
    if match:
        output = match.group().replace(",", "")
        return {"currency": output[0], "amount": float(output[1:])}

def zipcode(zip_string):
    match = re.search(r"^\d{5}$|^\d{5}\-\d{4}$", zip_string)
    if match:
        output = match.group()
        if "-" in output:
            return {"zip": output[0:5], "plus4": output[6:]}
        else:
            return {"zip": output[0:5], "plus4": None}

def date(date_string):
    date_regex = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
                  r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})",
                 ]
    for regex in date_regex:
        match = re.match(regex, date_string)
        if match:
            output = match.groupdict()
            for key in output:
                output[key] = int(output[key])
            return output
