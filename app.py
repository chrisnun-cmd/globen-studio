from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    """Recibe formulario de contacto."""
    nombre = request.form.get("nombre","").strip()
    email  = request.form.get("email","").strip()
    mensaje= request.form.get("mensaje","").strip()
    # Aquí se puede integrar envío de email más adelante
    return jsonify({"ok": True, "msg": "Mensaje recibido. Te contactamos en 48hrs."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
