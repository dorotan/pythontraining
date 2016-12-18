__author__ = 'dorota'
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Dorota", middle_name="Test", last_name="Test",
                      nickname="Test", title="abc", company="abc",
                      address="abc", home_number="123", mobile_number="123",
                      work_number="123", fax="123", first_email="a@a.pl",
                      second_email="b@b.pl", third_email="c@c.pl",
                      wwwpage="www.abc.pl",
                      birth_year="1986", anniversary_year="2016", second_address="def",
                      second_private_number="456", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)