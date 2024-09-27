# -Actividad-3---Arquitectura-Cliente-Servidor
Documentación externa del código:

Estructura del proyecto:

todo_app/
├── app.py
├── tasks.db
└── templates/
    └── index.html

    Descripción de los archivos:

`app.py`: Contiene el código del servidor Flask y la lógica de la aplicación.
`tasks.db`: Base de datos SQLite donde se almacenan las tareas.
`templates/index.html`: Plantilla HTML que define la interfaz de usuario.

Funcionamiento detallado:

a. Servidor (app.py):
Utiliza Flask para crear un servidor web en Python.
Implementa una base de datos SQLite para almacenar las tareas.
Define tres rutas principales:

GET /: Sirve la página principal (index.html).
GET /tasks: Recupera todas las tareas de la base de datos.
POST /tasks: Añade una nueva tarea a la base de datos.

La función `init_db()` se encarga de crear la tabla de tareas si no existe.

b. Cliente (index.html):

- Proporciona una interfaz de usuario simple con un campo de entrada y un botón.
- Utiliza JavaScript para manejar la interacción del usuario y comunicarse con el servidor.

- Funciones principales:

1. `addTask()`: Envía una nueva tarea al servidor mediante una solicitud POST.
2. `getTasks()`: Obtiene la lista de tareas del servidor mediante una solicitud GET y actualiza la interfaz.

Flujo de la aplicación:

1. El usuario accede a la página principal.
2. El servidor sirve el archivo index.html.
3. El cliente carga y muestra las tareas existentes.
4. El usuario puede agregar nuevas tareas:

   Ingresa el texto de la tarea y hace clic en "Agregar Tarea".
   El cliente envía la tarea al servidor.
   El servidor almacena la tarea en la base de datos.
   El cliente actualiza la lista de tareas mostrada.

Tecnologías utilizadas:

- Backend: Python con Flask
- Base de datos: SQLite
- Frontend: HTML, CSS, y JavaScript vanilla
- Comunicación cliente-servidor: API RESTful con Fetch API

Ventajas de la arquitectura cliente/servidor en este ejemplo:

- Separación clara de responsabilidades entre el cliente y el servidor.
- Procesamiento de datos en el servidor, lo que mejora la seguridad y eficiencia.
- Posibilidad de escalar el backend y frontend de forma independiente.
- Facilita la implementación de futuras características como autenticación o sincronización en tiempo real.

Posibles mejoras:

- Implementar autenticación de usuarios.
- Añadir la capacidad de editar y eliminar tareas.
- Mejorar el diseño de la interfaz de usuario.
- Implementar paginación para manejar grandes cantidades de tareas.
- Agregar validación de datos tanto en el cliente como en el servidor.
















