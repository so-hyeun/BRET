import os
import json
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template, url_for, send_file, send_from_directory
import subprocess
from predict_temp import chem_dis_func, drug2_func, gene_dis_func, return_result_ddi, return_result_gad, return_result_chemprot
from werkzeug.utils import redirect, secure_filename

UPLOAD_DIR = "static/result/"
INPUT_DIR = "dl/User_input/ori_input"
app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR
app.config['INPUT_DIR'] = INPUT_DIR
Bootstrap(app)
file_path = "result/"
app.config['FLAG'] = 'not Ready'  ##Ready상태면 업로드한 파일이 있다! 즉, 다운로드를 할 수 있다
app.config['OUTPUT_DIR'] = 'dl/User_output/'

@app.route('/')
def home():
    return render_template('index.html')





def download_chemdis(filename):
    return send_file(file_name,
                     attachment_filename='downloaded_file_name.csv',# 다운받아지는 파일 이름. 
                     as_attachment=True)


def download_drugdrug(filename):
    return send_from_directory(filename, filename="filename.txt")


def download_genedis(filename):
    return send_from_directory("static/result/GeneDis_result.txt", filename="filename.txt")


def predict_ddi(input_file):
    filename = input_file.split('.')[0]
    cmd = ["sh", "dl/predict_ddi.sh", "User_input/ori_input/"+input_file, filename]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()

def predict_chemprot(input_file):
    filename = input_file.split('.')[0]
    cmd = ["sh", "dl/predict_chemprot.sh", "User_input/ori_input/"+input_file, filename]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()
    
def predict_gad(input_file):
    filename = input_file.split('.')[0]+'.json'
    print("filename: "+filename)
    cmd = ["sh", "dl/predict_GAD.sh", "User_input/ori_input/"+input_file]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()

def model_performance_gad():
    with open('dl/model_result/gad_result.json') as json_file:
        json_data = json.load(json_file)
        model_performance = json_data['metrics']['PRF']
        f1 = model_performance.split('    ')[5]
    return str(f1)
    


@app.route('/Chemical-Disease', methods=['GET', 'POST'])
def ChemDis():
    
    if request.method == 'GET':
        return render_template('Chemical_Disease.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        input_file_path = os.path.join(app.config['INPUT_DIR'], fname)
        f.save(input_file_path)
        predict_chemprot(fname)
        result = return_result_chemprot(input_file_path,app.config['OUTPUT_DIR']+"Chem_Dis_result_"+fname )  # 이 함수에 사용자가 upload한 file
        
        
        return render_template('Chemical_Disease.html', model_result=result)

@app.route('/Drug-Drug', methods=['GET', 'POST'])
def DrugDrug():
    
    if request.method == 'GET':
        return render_template('Drug_Drug.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        input_file_path = os.path.join(app.config['INPUT_DIR'],fname)
        f.save(input_file_path)
        
        predict_ddi(fname)  # 이 함수에 사용자가 upload한 file
        result = return_result_ddi(input_file_path,app.config['OUTPUT_DIR']+"Drug_Drug_result_"+fname )
        
        return render_template('Drug_Drug.html', model_result=result)


@app.route('/Gene-Disease', methods=['GET', 'POST'])
def GeneDise():
    
    if request.method == 'GET':
        return render_template('Gene_Disease.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        input_file_path = os.path.join(app.config['INPUT_DIR'], fname)
        f.save(input_file_path)
        
        predict_gad(fname)
        result = return_result_gad(input_file_path,app.config['OUTPUT_DIR']+"Gene_Dis_result_"+fname )  # 이 함수에 사용자가 upload한 file
        performance = model_performance_gad()
        
        return render_template('Gene_Disease.html', model_result=result, model_performance=performance)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
