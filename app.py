from flask import Flask, render_template, jsonify, request
from supabase import create_client, Client
from config import supabase
import os

# Inicializar Flask
app = Flask(__name__)

# Conexión a Supabase
url = "https://mrourfyaunnpgscktcgu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1yb3VyZnlhdW5ucGdzY2t0Y2d1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3NDcwOTQsImV4cCI6MjA3NzMyMzA5NH0.hFSDH1LePrIOWlPkv4Qox54Jkr2umz6PvlzGI_F4YJM"
supabase: Client = create_client(url, key)

# ============================================================
# Página principal
@app.route('/')
def home():
    return render_template('index.html')

# ============================================================
# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        data = supabase.table("Usuarios").select("*").execute()
        return jsonify(data.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# Agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    try:
        nuevo_usuario = request.get_json()
        # Aseguramos que tenga los campos correctos
        usuario_data = {
            "nombre": nuevo_usuario.get("nombre"),
            "correo": nuevo_usuario.get("correo"),
            "telefono": nuevo_usuario.get("telefono")
        }
        response = supabase.table("Usuarios").insert(usuario_data).execute()
        return jsonify({"message": "Usuario agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# Actualizar un usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    try:
        datos = request.get_json()
        response = supabase.table("Usuarios").update(datos).eq("id", id).execute()
        return jsonify({"message": "Usuario actualizado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# Eliminar un usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        response = supabase.table("Usuarios").delete().eq("id", id).execute()
        return jsonify({"message": "Usuario eliminado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# Ejecutar servidor Flask (Render usa PORT)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
