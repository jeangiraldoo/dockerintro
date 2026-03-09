from flask import Flask
import os

app = Flask(__name__)

# Environment variables with fallback defaults
student = os.getenv("STUDENT_NAME", "Santiago")
# I chose Granada based on the professor's suggested neighborhoods
hood = os.getenv("BARRIO", "Granada") 

@app.get("/")
def home():
    """Main endpoint that returns the student info and logs the visit."""
    msg = f"Hola, I am {student} and I live in {hood}"
    
    # Open the shared volume log file in append mode
    with open("/var/log/app/visitas.log", "a") as f:
        f.write(msg + "\n")
        
    return msg

@app.get("/health")
def health():
    """Healthcheck endpoint used by Docker to verify container status."""
    return {"ok": True}, 200

if __name__ == "__main__":
    # Listen on all network interfaces on port 8080
    app.run(host="0.0.0.0", port=8080)