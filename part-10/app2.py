from flask import Flask,render_template,redirect,request 
from pymysql import connections
import pymysql
app=Flask(__name__)

#data base conntion using mysql 
db_Host="localhost"
db_user="root"
db_password="1234"
db_name="user2"

def connet_to_db():
    connecting=pymysql.connect(
       host=db_Host,
       user=db_user,
       password=db_password,
       database=db_name,
       cursorclass=pymysql.cursors.DictCursor
    )
    return connecting

@app.route("/")
def show():
    connection=connet_to_db()
    with connection.cursor() as cursor : 
        cursor.execute("SELECT * FROM table1")
        user = cursor.fetchall()
    connection.close() 
    return render_template("home.html",users=user)    

if "__main__"==__name__: 
    app.run(debug=True)

    


# from flask import Flask, render_template
# import pymysql

# app = Flask(__name__)

# # Database connection details
# db_Host = "localhost"
# db_user = "root"
# db_password = "1234"
# db_name = "user2"

# def connect_to_db():
#     connection = pymysql.connect(
#         host=db_Host,
#         user=db_user,
#         password=db_password,
#         database=db_name,
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     return connection

# @app.route("/")
# def show():
#     connection = connect_to_db()
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM table1")  # Correct SQL syntax
#             users = cursor.fetchall()
#     finally:
#         connection.close()  # Properly close the connection
#     return render_template("home.html", users=users)  # Pass users to template

# if __name__ == "__main__":
#     app.run(debug=True)
