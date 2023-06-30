from flask import Flask, render_template, url_for, request, flash, redirect, send_file


app = Flask(__name__)

# region img resource
@app.route('/images/<string:filename>', methods=['GET'])
def getimage(filename):
    path = 'static/img/' + filename
    return send_file(path)

# endregion


# region route
@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')
# endregion

if __name__ == "__main__":
    app.run(debug=True, threaded = True)
