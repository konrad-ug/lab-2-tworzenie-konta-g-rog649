from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=["POST"])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if not all(field in dane for field in ("imie", "nazwisko", "pesel")):
        return jsonify("Nie ma wszystkich pól"), 400

    if RejestrKont.wyszukaj_konto(dane["pesel"]):
        return jsonify("Konto już istnieje"), 400

    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=["GET"])
def ile_kont():
    return jsonify(RejestrKont.ile_kont()), 200


@app.route("/konta/konto/<pesel>", methods=["GET", "PUT", "DELETE"])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.wyszukaj_konto(pesel)
    if request.method != "DELETE" and not konto:
        return jsonify("Nie ma takiego konta"), 404

    if request.method == "PUT":
        RejestrKont.zmien_konto(pesel, request.get_json())
        return jsonify({}), 200
    elif request.method == "DELETE":
        RejestrKont.usun_konto(pesel)
        return jsonify({}), 200
    else:
        return (
            jsonify(
                imie=konto.imie,
                nazwisko=konto.nazwisko,
                pesel=konto.pesel,
                saldo=konto.saldo,
            ),
            200,
        )


@app.route("/konta/wyczysc", methods=["POST"])
def wyczysc_konta():
    RejestrKont.wyczysc_konta()
    return "", 200 if RejestrKont.ile_kont() == 0 else 500
