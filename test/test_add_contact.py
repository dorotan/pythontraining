# -*- coding: utf-8 -*-
__author__ = 'dorota'
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    test1 = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(test1) for i in range(random.randrange(maxlen))])

contact_data = [Contact(first_name="", middle_name="", last_name="", title="", company="", home_number="", work_number="", first_email="")]+[
    Contact(first_name=random_string("firstname", 20), middle_name=random_string("middlename", 20), last_name=random_string("lastname", 20),
            title=random_string("title", 20), company=random_string("company", 20), home_number=random_string("homenumber", 7),
            work_number=random_string("worknumber", 7), first_email=random_string("firstemail", 25))
    for i in range(5)
]

@pytest.mark.parametrize("contact", contact_data, ids=[repr(x)for x in contact_data])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)