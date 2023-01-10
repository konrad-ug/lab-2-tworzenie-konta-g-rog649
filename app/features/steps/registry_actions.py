from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"


@when(
    "I create an account using name: {name:S}, last name: {last_name:S}, pesel: {pesel:S}"
)
def create_account(context, name, last_name, pesel):
    json_body = {
        "imie": name.strip('"'),
        "nazwisko": last_name.strip('"'),
        "pesel": pesel.strip('"'),
    }
    create_response = requests.post(URL + "/konta/stworz_konto", json=json_body)
    assert_equal(create_response.status_code, 201)


@step("number of accounts in registry equals {count:d}")
def registry_account_count(context, count):
    ile_kont = requests.get(URL + f"/konta/ile_kont")
    assert_equal(ile_kont.json(), int(count))


@step("account with pesel {pesel:S} exists in registry")
def account_with_pesel_exists(context, pesel):
    pesel_strip = pesel.strip('"')
    response = requests.get(URL + f"/konta/konto/{pesel_strip}")
    account = response.json()
    assert_equal(response.status_code, 200)
    assert_equal(account["pesel"], pesel_strip)


@step("account with pesel {pesel:S} does not exist in registry")
def account_with_pesel_not_exist(context, pesel):
    pesel_strip = pesel.strip('"')
    response = requests.get(URL + f"/konta/konto/{pesel_strip}")
    assert_equal(response.status_code, 404)


@when("I update the last name of account with pesel {pesel:S} to {last_name:S}")
def update_last_name(context, pesel, last_name):
    pesel_strip = pesel.strip('"')
    last_name_strip = last_name.strip('"')
    requests.put(
        URL + f"/konta/konto/{pesel_strip}", json={"nazwisko": last_name_strip}
    )


@then("account with pesel {pesel:S} has last name {last_name:S}")
def account_has_last_name(context, pesel, last_name):
    pesel_strip = pesel.strip('"')
    last_name_strip = last_name.strip('"')
    response = requests.get(URL + f"/konta/konto/{pesel_strip}")
    account = response.json()
    assert_equal(response.status_code, 200)
    assert_equal(account["pesel"], pesel_strip)
    assert_equal(account["nazwisko"], last_name_strip)


@when("I delete account with pesel {pesel:S}")
def delete_account(context, pesel):
    pesel_strip = pesel.strip('"')
    response = requests.delete(URL + f"/konta/konto/{pesel_strip}")
    assert_equal(response.status_code, 200)


@when("I clear the account registry")
def delete_all_accounts(context):
    response = requests.post(URL + f"/konta/wyczysc")
    assert_equal(response.status_code, 200)
