import unittest
import requests

from ...RejestrKont import RejestrKont 

_account_body = {
    "imie": "Dariusz",
    "nazwisko": "Januszewski",
    "pesel": "87013092831"
}

_url = "http://localhost:5000"

class TestCreateAccount(unittest.TestCase):
    def test_create_account_correct(self):
        response = requests.post(_url + "/konta/stworz_konto", json=_account_body)
        self.assertEqual(response.status_code, 201, "Zły response!")

        requests.delete(_url + f"/konta/konto/{_account_body['pesel']}")

class TestAccountOperations(unittest.TestCase):
    def setUp(self):
        # Create an account to do the operations on
        requests.post(_url + "/konta/stworz_konto", json=_account_body)
    
    def tearDown(self):
        # Delete the account
        requests.delete(_url + f"/konta/konto/{_account_body['pesel']}")

    def test_get_account_pesel(self):
        # Get the account by PESEL and check if it's correct
        response = requests.get(_url + f"/konta/konto/{_account_body['pesel']}")
        self.assertEqual(response.status_code, 200, "Zły response!")

        response_body = response.json()
        self.assertEqual(response_body["imie"], _account_body["imie"], "Imię inne!")
        self.assertEqual(response_body["nazwisko"], _account_body["nazwisko"], "Nazwisko inne!")
        self.assertEqual(response_body["pesel"], _account_body["pesel"], "PESEL inne!")

    def test_edit_account(self):
        # Edit the account's name and check if it changed
        requests.put(
            _url + f"/konta/konto/{_account_body['pesel']}",
            json={
                "imie": "Grzegorz"
            }
        )

        read_response = requests.get(_url + f"/konta/konto/{_account_body['pesel']}")
        read_response_body = read_response.json()
        self.assertEqual(
            read_response_body["imie"],
            "Grzegorz",
            "Imię się nie zmieniło!"
        )
    
    def test_unique_pesel(self):
        # Don't create another account with the same PESEL
        create_response = requests.post(_url + "/konta/stworz_konto", json=_account_body)

        self.assertEqual(create_response.status_code, 400, "Zły status code!")
        self.assertTrue(create_response.json(), "Nie ma komunikatu błędu!")

    def test_delete_account(self):
        # Delete an account if it exists
        delete_response = requests.delete(_url + f"/konta/konto/{_account_body['pesel']}")
        self.assertEqual(delete_response.status_code, 200, "Zły status code!")
