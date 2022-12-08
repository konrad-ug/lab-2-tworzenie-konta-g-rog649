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
    
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201
    

@app.route("/konta/ile_kont", methods=["GET"])
def ile_kont():
    return jsonify(RejestrKont.ile_kont()), 200

@app.route("/konta/konto/<pesel>", methods=["GET", "PUT"])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.wyszukaj_konto(pesel)
    if not konto:
        return jsonify("Nie ma takiego konta"), 404 
    
    if request.method == "PUT":
        RejestrKont.zmien_konto(pesel, request.get_json())
        return jsonify({}), 202
    else:
        return jsonify(
            imie=konto.imie,
            nazwisko=konto.nazwisko,
            pesel=konto.pesel,
            saldo=konto.saldo
        ), 200
