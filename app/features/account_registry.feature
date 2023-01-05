Feature: Account registry
    Scenario: User is able to create a new account
        Given number of accounts in registry equals 0
        When I create an account using name: "kurt", last name: "cobain", pesel: "89091209875"
        Then number of accounts in registry equals 1
        And account with pesel "89091209875" exists in registry

    Scenario: User is able to create a second account
        Given number of accounts in registry equals 1
        When I create an account using name: "elvis", last name: "presley", pesel: "35010874691"
        Then number of accounts in registry equals 2
        And account with pesel "35010874691" exists in registry
    
    Scenario: User is able to delete already created account
        Given account with pesel "89091209875" exists in registry
        When I delete account with pesel "89091209875"
        Then account with pesel "89091209875" does not exist in registry
    
    Scenario: User is able to update last name saved in account
        Given account with pesel "35010874691" exists in registry
        When I update the last name of account with pesel "35010874691" to "parsley"
        Then account with pesel "35010874691" has last name "parsley"

    Scenario: Admin user is able to clear the account registry
        When I clear the account registry
        Then number of accounts in registry equals 0
