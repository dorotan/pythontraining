__author__ = 'dorota'
from model.group import Group


def test_modify_group_name(app):
    if app.group.count1() > 0:
        app.group.create(Group(name="ABC"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count1() > 0:
        app.group.create(Group(header="ABC"))
    app.group.modify_first_group(Group(header="New header"))