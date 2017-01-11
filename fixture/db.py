__author__ = 'dorota'
import mysql.connectorb
from model.group import Group
from model.contact import Contact


class DbFixture:


    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, nickname, company, title, address, fax, notes from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, nickname, firstname, lastname, company, title, address, fax, notes) = row
                list.append(Contact(id=id, nickname=nickname, firstname=firstname, lastname=lastname, company=company,
                                    title=title, address=address, fax=fax, notes=notes))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()


