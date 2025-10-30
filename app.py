from flask import Flask, render_template, jsonify, request
from supabase import create_client, Client
import os

app = Flask(__name__)

# Configura tu conexión Supabase
url = "https://mrourfyaunnpgscktcgu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1yb3VyZnlhdW5ucGdzY2t0Y2d1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3NDcwOTQsImV4cCI6MjA3NzMyMzA5NH0.hFSDH1LePrIOWlPkv4Qox54Jkr2umz6PvlzGI_F4YJM"
supabase: Client = create_client(url, key)

@app.route('/')
def home():
    return render_template('index.html')

# 📋 Leer todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        data = supabase.table("Usuarios").select("*").execute()
        return jsonify(data.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ➕ Agregar usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    try:
        nuevo_usuario = request.get_json()
        print("📩 Recibido:", nuevo_usuario)
        response = supabase.table("Usuarios").insert({
            "nombre": nuevo_usuario["nombre"],
            "correo": nuevo_usuario["correo"],
            "telefono": nuevo_usuario["telefono"]
        }).execute()
        return jsonify({"message": "Usuario agregado correctamente"}), 201
    except Exception as e:
        print("❌ Error al agregar:", e)
        return jsonify({"error": str(e)}), 500

# ✏️ Actualizar usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    try:
        datos = request.get_json()
        print("✏️ Actualizando ID:", id, "con", datos)
        response = supabase.table("Usuarios").update(datos).eq("id", id).execute()
        return jsonify({"message": "Usuario actualizado correctamente"})
    except Exception as e:
        print("❌ Error al actualizar:", e)
        return jsonify({"error": str(e)}), 500

# ❌ Eliminar usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        print("🗑 Eliminando ID:", id)
        response = supabase.table("Usuarios").delete().eq("id", id).execute()
        return jsonify({"message": "Usuario eliminado correctamente"})
    except Exception as e:
        print("❌ Error al eliminar:", e)
        return jsonify({"error": str(e)}), 500

# Servidor Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
