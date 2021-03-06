__author__ = 'dorota'
# -*- coding: utf-8 -*-
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname[3], last_name=lastname, id=id,
                                                  all_phones_from_homepage = all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        second_private_number = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id,
                       home_number=home_number, work_number=work_number,
                       mobile_number=mobile_number, second_private_number=second_private_number,
                       email = email, email2 = email2, email3 = email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        second_private_number = re.search("P: (.*)", text).group(1)
        return Contact(home_number=home_number, work_number=work_number,
                       mobile_number=mobile_number, second_private_number=second_private_number)


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("nowy wpis").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_number)
        self.change_field_value("mobile", contact.mobile_number)
        self.change_field_value("work", contact.work_number)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.first_email)
        self.change_field_value("email2", contact.second_email)
        self.change_field_value("email3", contact.third_email)
        self.change_field_value("homepage", contact.wwwpage)
        self.change_field_value("byear", contact.birth_year)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.second_address)
        self.change_field_value("phone2", contact.second_private_number)
        self.change_field_value("notes", contact.notes)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # open modification form
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % str(id)).click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_contact_by_index(index)
        # confirm deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_contact_by_id(id)
        # confirm deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def add_contact_to_group_by_id(self, id, group):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        number = group.id
        wd.find_element_by_xpath("//select[@name='to_group']//option[@value='%s']" % number).click()
        wd.find_element_by_name("add").click()
        self.app.open_home_page()
        self.contact_cache = None

    def add_contact_to_group(self, Contact, group):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        number = group.id
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[@value='%s']" % number).click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        contact_row = wd.find_elements_by_name("entry")[index]
        contact_cell = contact_row.find_elements_by_tag_name("td")
        contact_cell[7].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("index.php") and len(wd.find_elements_by_id("MassCB")) > 0):
            wd.find_element_by_link_text("strona główna").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_if_list_contains_removed_contacts(self, old_contacts, removed_contacts):
        if sorted(removed_contacts, key=Contact.id_or_max) in sorted(old_contacts, key=Contact.id_or_max):
            old_contacts.remove(removed_contacts)
        return old_contacts
