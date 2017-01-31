*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=   Get Contact List
    ${contact}=  New Contact  firstname1  lastname1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List    ${old_list}  ${contact}
    Contact List Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=   Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate   random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact   ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact List Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=   Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate   random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${contact1}=  New Contact  firstname1  lastname1
    Modify Contact   ${contact}  ${contact1}
    ${new_list}=  Get Contact List
    Contact List Should Be Equal  ${new_list}  ${old_list}