__author__ = 'dorota'
# -*- coding: utf-8 -*-
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

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

    def modify_first_contact(self):
        self.modify_contact_by_index[0]

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        contactrow = wd.find_elements_by_name("entry")[index]
        contactcell = contactrow.find_elements_by_tag_name("td")
        contactcell[7].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("index.php") and len(wd.find_elements_by_id("MassCB")) > 0):
            wd.find_element_by_link_text("strona główna").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count1(self):
        wd = self.app.wd
        self.open_new_contact_page()
        return len(wd.find_elements_by_name("update"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                contactcell = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=contactcell[2].text, id=id))
        return list(self.contact_cache)