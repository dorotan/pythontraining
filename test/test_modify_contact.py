__author__ = 'dorota'
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count1() > 0:
        app.contact.create(Contact(firstname="Dorota"))
    app.contact.modify_first_contact(Contact(firstname="Robert"))


def test_modify_contact_middlename(app):
    if app.contact.count1() > 0:
        app.contact.create(Contact(middlename="Kowal"))
    app.contact.modify_first_contact(Contact(middlename="Nowak"))