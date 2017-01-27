import re
from model.contact import Contact


def all_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Dorota", last_name="Test"))
    name_from_home_page = app.contact.get_contact_list()[0]
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    lastname_from_home_page = app.contact.get_contact_list()[0]
    lastname_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    address_from_home_page = app.contact.get_contact_list()[0]
    address_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert lastname_from_home_page.last_name == lastname_from_edit_page.last_name
    assert name_from_home_page.address == name_from_edit_page.address
    assert address_from_home_page.address == address_from_edit_page.address

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.work_number, contact.mobile_number, contact.second_private_number]))))