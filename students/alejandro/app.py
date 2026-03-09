from flask import Flask
import os

app = Flask(__name__)
student = os.getenv("STUDENT_NAME", "Anon") #lee variable de entorno STUDENT_NAME, si no existe usa "Anon" como degfault
hood = os.getenv("BARRIO", "Unknown")

@app.get("/")
def home():
    msg = f"Hola, I am {student} and I live in {hood}"
    with open("/var/log/app/visitas.log", "a") as f: #abre el archivo visitas.log en modo append, volumen compartido?
        f.write(msg + "\n")
    return msg

@app.get("/health")
def health():
    return {"ok": True}, 200 #consulta cada 200 segundos si el contenedor esta vivo, el metodo devuelve un json y se reinicia?

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)