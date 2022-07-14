# https://qiita.com/NAKA_G/items/f34738df364af8cbd58e

from flask import Flask, render_template, request, redirect, url_for
from Intro_don import IntroDon
instance_introdon = IntroDon()


UPLOAD_FOLDER = '/mp3'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
host='0.0.0.0'

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
    # return render_template('start.html')

@app.route('/start')
def start():
    instance_introdon.reset()
    return render_template('start.html')

@app.route('/problem',methods = ["GET"])
def problem():
    sent_wav, choices_names_list = instance_introdon.Move2NextProblem()
    numberProblem = instance_introdon.GetNowProblem()
    numCorrect = instance_introdon.GetPoint()
    return render_template('problem.html',choices_names_list=choices_names_list,sent_wav=sent_wav,numberProblem=numberProblem,numCorrect=numCorrect)

@app.route('/problem',methods = ["POST"])
def answer():
    print("request.method: ", request.method)
    test_ans = int(request.form["radio"])
    print("request.form['send']: ", test_ans)
    result_flag = instance_introdon.AnswerTheQuestion(test_ans)
    print("result_flag: ",result_flag)
    numberProblem = instance_introdon.GetNowProblem()
    numCorrect = instance_introdon.GetPoint()
    if result_flag:
        JudgeWord = "正解！！"
    else:
        JudgeWord = "残念！！"
    return render_template('answer.html',numberProblem=numberProblem,numCorrect=numCorrect,result_flag=result_flag,JudgeWord=JudgeWord)

@app.route('/sum_point')
def sum_point():
    numCorrect = instance_introdon.GetPoint()
    return render_template('sum_point.html',numCorrect=numCorrect)

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(debug=True, host=host, port=801)
    app.run()