from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
