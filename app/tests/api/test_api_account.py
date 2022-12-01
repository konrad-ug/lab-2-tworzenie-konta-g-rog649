import unittest
import requests

class TestCreateAccount(unittest.TestCase):
    body = {
        "imie": "Dariusz",
        "nazwisko": "Januszewski",
        "pesel": "87013092831"
    }

    url = "localhost:5000"

    def test_create_account_correct(self):
        response = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(response.status_code, 201, "Zły response!")
    
    def test_get_account_pesel(self):
        response = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(response.status_code, 200, "Zły response!")

        response_body = response.json()
        self.assertEqual(response_body["imie"], self.body["imie"], "Imię inne!")
        self.assertEqual(response_body["nazwisko"], self.body["nazwisko"], "Nazwisko inne!")
        self.assertEqual(response_body["pesel"], self.body["pesel"], "PESEL inne!")

    def test_edit_account(self):
        requests.post(self.url + "/konta/stworz_konto", json=self.body)
        update_response = requests.put(
            self.url + f"/konta/konto/{self.body['pesel']}",
            json={
                "imie": "Grzegorz"
            }
        )
        read_response = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        read_response_body = read_response.json()
        self.assertEqual(
            read_response_body["imie"],
            "Grzegorz",
            "Imię się nie zmieniło!"
        )