from flask import Flask, render_template, request
import mysql.connector as msc

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def add_user():
    message = ""

    
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password","")  # No .strip() yet—we'll encode carefully later

        conn = msc.connect(
            host="localhost",
            user="root",
            password="09112004",
            database="sumit",
        )
        try:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",(username,password)
                )
                
            conn.commit()  # Commit the transaction! Without this, nothing sticks.
            message = f"{username} added successfully."

            cursor.close()
        finally:
            conn.close()

    return render_template("add_user.html", message=message)

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    return render_template("reset_password.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
