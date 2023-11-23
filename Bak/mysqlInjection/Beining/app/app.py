from flask import Flask, render_template,request
import mysql.connector
import db_conn

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Set up the MySQL connection
db_connection = mysql.connector.connect(
    host= db_conn.host,
    user= db_conn.user,
    password= db_conn.password,
    database= db_conn.database
)
db_cursor = db_connection.cursor()


def shitSql(name,password):

    # Use parameterized query to prevent SQL injection
    sql_query = 'SELECT * FROM Userdata WHERE name = %s AND password = %s'
    db_cursor.execute(sql_query, (name, password))

    results =db_cursor.fetchall()
    db_connection.close()
    return results

@app.route("/", methods=["GET", "POST"]) 
def index():
    if request.method== "POST":
        name=request.form["name"]
        password=request.form["password"]
        return shitSql(name,password)
        
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)