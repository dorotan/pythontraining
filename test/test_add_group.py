# -*- coding: utf-8 -*-
__author__ = 'dorota'
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    test1 = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(test1) for i in range(random.randrange(maxlen))])


group_data = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

@pytest.mark.parametrize("group", group_data, ids=[repr(x)for x in group_data])

def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)