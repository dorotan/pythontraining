__author__ = 'dorota'
from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="ABC"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Robert")
    contact.id = old_contacts[index].id
    if app.contact.count1() < 0:
        app.contact.create(Contact(firstname="Dorota"))
    app.contact.modify_contact_by_index(contact, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count1() < 0:
#        app.contact.create(Contact(middlename="Kowal"))
#    app.contact.modify_first_contact(Contact(middlename="Nowak"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)