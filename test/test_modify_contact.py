__author__ = 'dorota'
from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Robert")
    contact.id = old_contacts[0].id
    if app.contact.count1() < 0:
        app.contact.create(Contact(firstname="Dorota"))
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count1() < 0:
#        app.contact.create(Contact(middlename="Kowal"))
#    app.contact.modify_first_contact(Contact(middlename="Nowak"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)