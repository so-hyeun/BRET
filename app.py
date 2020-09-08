import os
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template, url_for

from predict_temp import chem_dis_func,drug2_func,gene_dis_func
from werkzeug.utils import redirect, secure_filename

UPLOAD_DIR = "static/result/"

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Chemical_Disease.html',methods=['GET','POST'])
def ChemDis():
    if request.method == 'GET':
        return render_template('Chemical_Disease.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        path = app.config['UPLOAD_DIR']+fname
        f.save(path)
        result = chem_dis_func("file ") #이 함수에 사용자가 upload한 file

        return render_template('Chemical_Disease.html', model_result=result)

    

@app.route('/Drug_Drug.html', methods=['GET','POST'])
def DrugDrug():
    if request.method == 'GET':
        return render_template('Drug_Drug.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        path = app.config['UPLOAD_DIR']+fname
        f.save(path)
        result = drug2_func("file ") #이 함수에 사용자가 upload한 file

        return render_template('Drug_Drug.html', model_result=result)



@app.route('/Gene_Disease.html', methods=['GET','POST'])
def GeneDise():
    if request.method == 'GET':
        return render_template('Gene_Disease.html')
    elif request.method == 'POST':
        f = request.files['fileToUpload']
        fname = secure_filename(f.filename)
        path = app.config['UPLOAD_DIR']+fname
        f.save(path)
        result = gene_dis_func("file ") #이 함수에 사용자가 upload한 file

        return render_template('Gene_Disease.html', model_result=result)

@app.route('/contact.html')
def contact():
    return render_template('contact.html')




if __name__ == "__main__":
    app.run(debug=True)
