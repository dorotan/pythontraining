__author__ = 'dorota'
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.open_homepage()

    def open_homepage(self):
        def open_home_page(self):
            wd = self.wd
            if not (wd.current_url.endswith("index.php") and len(wd.find_elements_by_link_text("CREATE_ACCOUNT")) > 0):
                wd.get("http://localhost:81/addressbook")
            pass

    def destroy(self):
        self.wd.quit()