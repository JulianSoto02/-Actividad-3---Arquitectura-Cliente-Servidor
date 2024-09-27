from flask import Flask, request, jsonify, render_template
import sqlite3

# Inicializar la aplicación Flask
app = Flask(__name__)

def init_db():
    """
    Inicializa la base de datos SQLite y crea la tabla de tareas si no existe.
    """
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Llamar a init_db() para asegurar que la base de datos esté creada
init_db()

@app.route('/')
def index():
    """
    Ruta principal que renderiza la plantilla index.html.
    """
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Obtiene todas las tareas de la base de datos y las devuelve como JSON.
    """
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = [row[1] for row in c.fetchall()]  # Extraer solo el texto de la tarea
    conn.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Añade una nueva tarea a la base de datos.
    Espera recibir un JSON con la clave 'task'.
    """
    task = request.json['task']
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarea agregada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
