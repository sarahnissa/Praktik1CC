from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return f"<h2>Halo {name}, email Anda {email} telah diterima.</h2>"
    
    return '''
        <form method="post">
            Nama: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
