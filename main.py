from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

names = ['Uncle', 'Mom']
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == POST:
        variable = request.form['information']
        return render_template('index.html', information='I love flask.', names=names, variabl=variable)
    return render_template('index.html', information='I love Flask.')
if __name__ == "main":
    app.run(debug=True)
