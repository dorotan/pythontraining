__author__ = 'dorota'

from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("nowy wpis").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # fill new contact form
        self.fill_contact_form(contact)
        # submit adding new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_xpath("//div/div[3]/ul/li[1]/a").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.get("http://localhost:81/addressbook/")
        wd.find_element_by_name("selected[]").click()
        # open modification form
        wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[11]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def change_field_value_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("address2", contact.address2)
        self.change_field_value_contact("phone2", contact.phone2)
        self.change_field_value_contact("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.open_new_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count1(self):
        wd = self.app.wd
        self.open_new_contact_page()
        return len(wd.find_elements_by_name("update"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_new_contact_page()
            contacts = []
            for element in wd.find_elements_by_css_selector("td.center"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(name=text, id=id))
        return list(self.contact_cache)