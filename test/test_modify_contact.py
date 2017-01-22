__author__ = 'dorota'
# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Dorota", last_name="Test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(first_name="Robert", last_name="Nowak")
    contact.id = old_contact.id
    app.contact.modify_contact_by_id(old_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)