from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == "main":
    app.run(debug=True)
