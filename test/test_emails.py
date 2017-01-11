def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email2 == contact_from_edit_page.email2
    assert contact_from_home_page.email3 == contact_from_edit_page.email3