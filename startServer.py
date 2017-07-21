

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import classify

UPLOAD_FOLDER = dir_path
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.run(host="0.0.0.0")
# app.run(threaded=True)

@app.route('/')
def root():
    return app.send_static_file('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files['image']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return classify.run(os.path.join(app.config['UPLOAD_FOLDER']+"/"+filename))
