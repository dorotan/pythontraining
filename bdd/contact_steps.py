__author__ = 'dorota'
from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <first_name>, <middle_name>, <last_name>, <title>, <company>, <address>, <home_number> and <first_email>')
def newcontact(first_name, middle_name, last_name, title, company, address, home_number, first_email):
    return Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, title=title, company=company, address=address,
                   home_number=home_number, first_email=first_email)

@when('I add the contact to the list')
def add_new_contact(app, newcontact):
    app.contact.create(newcontact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, new_contact_list):
    old_contacts = new_contact_list
    new_contact_list = db.get_contact_list()
    old_contacts.append(new_contact_list)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.modify_first_contact(Contact(first_name="Dorota", last_name="Test"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@given('a contact with <first_name>, <middle_name>, <last_name>, <title>, <company>, <address>, <home_number> and <first_email>')
def new_contact(first_name, middle_name, last_name, title, company, address, home_number, first_email):
    return Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, title=title, company=company, address=address,
                   home_number=home_number, first_email=first_email)

@when('I modify the contact in the list')
def modify_some_contact(app, random_contact, new_contact):
    app.contact.modify_contact_by_id(random_contact.id, new_contact)

@then('the modified contact list is equal to the old list')
def verify_contact_modified(db, app, check_ui):
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(first_name="Robert", last_name="Nowak")
    contact.id = old_contact.id
    app.contact.modify_contact_by_index(old_contact.id, contact)
    new_contacts = db.get_contact_list()
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
