from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    full_name = 'Aidas Gaučas'
    email = 'aidasgau2@gmail.com'
    github = 'https://github.com/aidasgau'
    current_year = datetime.datetime.now().year
    return render_template('home.html', current_year=current_year, full_name=full_name, email=email, github=github)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)