# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="ab", middlename="cd", lastname="ef", nickname="gh", mobile="123",
                               email="", address2="", phone2="", notes=""))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", mobile="",
                               email="", address2="", phone2="", notes=""))
    app.session.logout()
