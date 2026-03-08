from flask import Flask
import os

app = Flask(__name__)

student = os.getenv("STUDENT_NAME", "Esteban")
hood = os.getenv("BARRIO", "Bonanza,city")

@app.route("/")
def home():
    msg = f"Hola, Soy {student} and I live in {hood}"

    with open("/var/log/app/visitas.log", "a") as f:
        f.write(msg + "\n")

    return msg

@app.route("/health")
def health():
    return {"ok": True}

app.run(host="0.0.0.0", port=8080)