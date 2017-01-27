import re
from model.contact import Contact

def all_emails_on_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email2 == contact_from_edit_page.email2
    assert contact_from_home_page.email3 == contact_from_edit_page.email3
    assert email_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(email_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.first_email, contact.second_email, contact.third_email]))))