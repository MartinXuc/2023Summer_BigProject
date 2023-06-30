from flask import Flask, render_template


app = Flask(__name__)


# region route
@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')
# endregion

if __name__ == "__main__":
    app.run(debug=True, threaded = True)
