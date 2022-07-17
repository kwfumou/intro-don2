# https://qiita.com/NAKA_G/items/f34738df364af8cbd58e

from flask import Flask, render_template, request, redirect, url_for
# from Intro_don import IntroDon
# instance_introdon = IntroDon()


UPLOAD_FOLDER = '/mp3'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
host='0.0.0.0'

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/problem')
def problem():
    return render_template('problem.html')

@app.route('/sum_point')
def sum_point():
    return render_template('sum_point.html')

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(debug=True, host=host, port=801)
    app.run()