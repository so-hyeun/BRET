# -*- coding: utf-8 -*- 
import os
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template, url_for, send_file, send_from_directory
import subprocess
from predict_temp import chem_dis_func, drug2_func, gene_dis_func
from werkzeug.utils import redirect, secure_filename

UPLOAD_DIR = "static/result/"
INPUT_DIR = "dl/User_input/ori_input"
app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR
app.config['INPUT_DIR'] = INPUT_DIR
Bootstrap(app)
file_path = "result/"
app.config['FLAG'] = 'not Ready'  


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Chemical-Disease', methods=['GET', 'POST'])
def ChemDis():
    if 'download' in request.form and app.config['FLAG'] == "Ready":
        download_chemdis("static/result/ChemDis-result.txt")
    if request.method == 'GET':
        return render_template('Chemical_Disease.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)

        result = chem_dis_func("file ")  # 이 함수에 사용자가 upload한 file
        fw = open("static/result/ChemDis_result.txt", 'w')
        fw.write(result)
        app.config['FLAG'] = 'Ready'
        return render_template('Chemical_Disease.html', model_result=result)


def download_chemdis(filename):
    return send_from_directory("static/result/ChemDis_result.txt", filename="Chemical_Disease.txt")


def download_drugdrug(filename):
    return send_from_directory("static/result/DrugDrug_result.txt", filename="filename.txt")


def download_genedis(filename):
    return send_from_directory("static/result/GeneDis_result.txt", filename="filename.txt")


def hello(input_file):
    cmd = ["sh", "dl/predict.sh", "User_input/ori_input/"+input_file]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()
    print(err)
    return str(out)

def for_show():
    cmd = ["python", "dl/show.py"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()
    print(err)
    return str(out)


@app.route('/Drug-Drug', methods=['GET', 'POST'])
def DrugDrug():
    if 'download' in request.form:
        download_chemdis("static/result/DrugDrug_result.txt")
    if request.method == 'GET':
        return render_template('Drug_Drug.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        input_file_path = os.path.join(app.config['INPUT_DIR'], fname)
        f.save(input_file_path)

        hello(fname)  # 이 함수에 사용자가 upload한 file
        result = for_show()
        fw = open("dl/User_output/DrugDrug_result.txt", 'w')  # predict result 저장 위치
        fw.write(result)
        print("Result: "+result)
        return render_template('Drug_Drug.html', model_result=result)


@app.route('/Gene-Disease', methods=['GET', 'POST'])
def GeneDise():
    if 'download' in request.form:
        download_chemdis("static/result/GeneDis_result.txt")
    if request.method == 'GET':
        return render_template('Gene_Disease.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)

        result = gene_dis_func("file ")  # 이 함수에 사용자가 upload한 file
        fw = open("static/result/GeneDis_result.txt", 'w')
        fw.write(result)
        return render_template('Gene_Disease.html', model_result=result)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
