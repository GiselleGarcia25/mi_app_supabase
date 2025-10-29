from flask import Flask, jsonify, request
from supabase import create_client, Client

# Inicializar la app Flask
app = Flask(__name__)

# 🔹 Conexión a Supabase
# (Copia tus datos desde Project Settings > API)
url = "https://mrourfyaunnpgscktcgu.supabase.co"  # 👉 Tu Project URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1yb3VyZnlhdW5ucGdzY2t0Y2d1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3NDcwOTQsImV4cCI6MjA3NzMyMzA5NH0.hFSDH1LePrIOWlPkv4Qox54Jkr2umz6PvlzGI_F4YJM"               # 👉 Tu anon public key
supabase: Client = create_client(url, key)

# ============================================================
# 🧩 RUTA PRINCIPAL
@app.route('/')
def home():
    return "🚀 Servidor Flask corriendo correctamente con Supabase."

# ============================================================
# 📋 LEER TODOS LOS USUARIOS (GET)
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        data = supabase.table("Usuarios").select("*").execute()
        return jsonify(data.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# ➕ CREAR UN NUEVO USUARIO (POST)
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    try:
        nuevo_usuario = request.get_json()
        response = supabase.table("Usuarios").insert(nuevo_usuario).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# ✏️ ACTUALIZAR UN USUARIO (PUT)
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    try:
        datos = request.get_json()
        response = supabase.table("Usuarios").update(datos).eq("id", id).execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# ❌ ELIMINAR UN USUARIO (DELETE)
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        response = supabase.table("Usuarios").delete().eq("id", id).execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# 🚀 Ejecutar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True, port=5001)

