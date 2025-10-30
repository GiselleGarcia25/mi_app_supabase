from flask import Flask, request, render_template, redirect, url_for
from supabase import create_client, Client

app = Flask(__name__)

# Configura tu conexión a Supabase
url = "https://TU_URL_SUPABASE.supabase.co"
key = "TU_API_KEY_SUPABASE"
supabase: Client = create_client(url, key)

# Ruta principal: muestra los datos
@app.route('/')
def index():
    data = supabase.table("Usuarios").select("*").execute()
    usuarios = data.data
    return render_template("index.html", usuarios=usuarios)

# Ruta para agregar usuario
@app.route('/agregar', methods=['POST'])
def agregar():
    id = request.form['id']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    
    supabase.table("Usuarios").insert({
        "id": id,
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }).execute()
    
    return redirect(url_for('index'))

# Ruta para eliminar usuario
@app.route('/eliminar/<int:id>')
def eliminar(id):
    supabase.table("Usuarios").delete().eq("id", id).execute()
    return redirect(url_for('index'))

# Ruta para modificar usuario (selección de campo)
@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    if request.method == 'POST':
        campo = request.form['campo']
        nuevo_valor = request.form['nuevo_valor']

        # Actualiza dinámicamente el campo que el usuario elige
        supabase.table("Usuarios").update({campo: nuevo_valor}).eq("id", id).execute()
        return redirect(url_for('index'))
    
    return render_template("modificar.html", id=id)

if __name__ == '__main__':
    app.run(debug=True)

