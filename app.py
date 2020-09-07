from flask import Flask, request, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Chemical_Disease.html')
def ChemDis():
    return render_template('Chemical_Disease.html')

@app.route('/Drug_Drug.html', methods=['GET','POST'])
def DrugDrug():
    if request.method == 'GET':
        return render_template('Drug_Drug.html')
    elif request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

@app.route('/Gene_Disease.html')
def GeneDise():
    return render_template('Gene_Disease.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
