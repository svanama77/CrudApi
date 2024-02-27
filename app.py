from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'saisrujan'
app.config['MYSQL_PASSWORD'] = 'saisrujan'
app.config['MYSQL_DB'] = 'backend'

mysql = MySQL(app)

# Create
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    title = data['title']
    completed = data['completed']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO todos (title, completed) VALUES (%s, %s)", (title, completed))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Todo created successfully"})

# Read
@app.route('/todos', methods=['GET'])
def get_todos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM todos")
    todos = cur.fetchall()
    cur.close()

    return jsonify(todos)

# Update
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    title = data['title']
    completed = data['completed']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE todos SET title = %s, completed = %s WHERE id = %s", (title, completed, todo_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Todo updated successfully"})

# Delete
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Todo deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
