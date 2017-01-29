Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first_name>, <middle_name>, <last_name>, <title>, <company>, <address>, <home_number> and <first_email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first_name  | middle_name  |  last_name  |  title  |  company  |  address  |  home_number  |  first_email  |
  | first_name1  | middle_name1  |  last_name1  |  title1  |  company1  |  address1  |  home_number1  |  first_email1  |
  | first_name2  | middle_name2  |  last_name2  |  title2  |  company2  |  address2  |  home_number2  |  first_email2  |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <first_name>, <middle_name>, <last_name>, <title>, <company>, <address>, <home_number> and <first_email>
  When I modify the contact in the list
  Then the modified contact list is equal to the old list