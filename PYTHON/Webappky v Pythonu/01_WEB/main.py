from flask import Flask, render_template, request, jsonify
from random import randint
import time
import os

app = Flask(__name__)

start_time = time.time()

quiz_questions = [
    {
        "question": "Jaké auto si stavíš ze začátku?",
        "options": {
            "A": "Satsuma",
            "B": "Ferndale",
            "C": "Gifu"
        },
        "correct": "A"
    },
    {
        "question": "Co se stane, když ve hře umřeš?",
        "options": {
            "A": "Hra se zavře",
            "B": "Objevíš se před kostelem",
            "C": "Vymaže ti top všechno na disku"
        },
        "correct": "B"
    },
    {
        "question": "Čím můžeš doplnit pivo, když ti dojde?",
        "options": {
            "A": "Ničím",
            "B": "Mlékem",
            "C": "Vodou"
        },
        "correct": "A"
    },
    {
        "question": "Kde bydlí opravář Fleetari?",
        "options": {
            "A": "Vedle doma hráče",
            "B": "v Teimo obchodě",
            "C": "V domě vedle zastávky"
        },
        "correct": "C"
    },
    {
        "question": "K čemu slouží vozidlo Gifu?",
        "options": {
            "A": "Na rozvoz jídla",
            "B": "Na vyvážení septiků",
            "C": "Na přepravu dřeva"
        },
        "correct": "B"
    },
    {
        "question": "Co se stane, když necháš baterii připojenou přes noc a motor neběží?",
        "options": {
            "A": " Nabije se",
            "B": "Baterie se vybije",
            "C": "Nic se nestane"
        },
        "correct": "B"
    }
]


# Ukládání počtu návštěv do souboru
VISIT_COUNT_FILE = "visit_count.txt"

# Funkce pro načítání počtu návštěv z textového souboru
def load_visit_count():
    if os.path.exists(VISIT_COUNT_FILE):
        with open(VISIT_COUNT_FILE, "r") as f:
            return int(f.read())
    return 0

# Funkce pro uložení počtu návštěv do souboru
def save_visit_count(count):
    with open(VISIT_COUNT_FILE, "w") as f:
        f.write(str(count))

# Načítání počtu návštěv při spuštění serveru
visit_count = load_visit_count()

# Funkce pro zvýšení počtu návštěv, bude spuštěna při každém požadavku na jakoukoli stránku
@app.before_request
def before_request():
    global visit_count
    # Zvýšení počtu návštěv při každém požadavku na jakoukoli stránku
    visit_count += 1
    save_visit_count(visit_count)


@app.route("/")
def home():
    name = "Petr"
    age = randint(10, 80)
    return render_template("home.html", user_name=name, user_age=age)

@app.route("/repo")
def about():
    return render_template("repo.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    result = None
    correct_count = 0

    if request.method == "POST":
        for i, q in enumerate(quiz_questions):
            user_answer = request.form.get(f"q{i}")
            if user_answer == q["correct"]:
                correct_count += 1
        result = f"Máš {correct_count} správných odpovědí z {len(quiz_questions)}!"

    return render_template("quiz.html", questions=quiz_questions, result=result)

@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/about")
def contact():
    return render_template("about.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/stats")
def stats():
    # Získání času běhu serveru
    uptime = time.time() - start_time
    return render_template("stats.html", uptime=uptime, visit_count=visit_count)

@app.route("/server_info")
def server_info():
    # Endpoint pro vrácení statistik serveru ve formátu JSON
    uptime = time.time() - start_time
    return jsonify({
        'uptime': uptime,
        'visit_count': visit_count
    })


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.2')
