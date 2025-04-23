from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <--- habilita CORS para todas las rutas

@app.route("/")
def index():
    return jsonify({
        "name": "Docx API",
        "version": "1.0.0",
        "description": "API para reemplazar texto en archivos .docx"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)