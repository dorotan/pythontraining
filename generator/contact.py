from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", work_number="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 20),
            last_name=random_string("last_name", 20), nickname=random_string("nickname", 10),
            address=random_string("address", 10), home_number=random_string("home_number", 5),
            mobile_number=random_string("mobile_number", 10), work_number=random_string("work_number", 20),
            fax=random_string("fax", 10), first_email=random_string("first_email", 10),
            second_email=random_string("second_email", 10), third_email=random_string("third_email", 10),
            wwwpage=random_string("wwwpage", 10), birth_year=random_string("birth_year", 4),
            anniversary_year=random_string("anniversary_year", 4), second_address=random_string("second_address", 20),
            second_private_number=random_string("second_private_number", 10), notes=random_string("notes", 10))
    for work_number in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__))