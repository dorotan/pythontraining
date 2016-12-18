__author__ = 'dorota'
# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home_number=None,
                 mobile_number=None, work_number=None, fax=None, first_email=None, second_email=None, third_email=None, wwwpage=None, birth_year=None,
                 anniversary_year=None, second_address=None, second_private_number=None, notes=None, id= None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.fax = fax
        self.first_email = first_email
        self.second_email = second_email
        self.third_email = third_email
        self.wwwpage = wwwpage
        self.birth_year = birth_year
        self.anniversary_year = anniversary_year
        self.second_address=second_address
        self.second_private_number = second_private_number
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(con):
        if con.id:
            return int(con.id)
        else:
            return maxsize