import os

from werkzeug.utils import secure_filename
import urllib.request

from flask import Flask, render_template, request, redirect, flash, url_for
from flask import Flask


from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.mobilenet import preprocess_input
from keras.applications.mobilenet import decode_predictions
from keras.applications.mobilenet import MobileNet


def getPrediction(filename):

    model = MobileNet()
    image = load_img('images/'+filename, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    label = label[0][0]
    print('%s (%.2f%%)' % (label[1], label[2]*100))
    return label[1], label[2]*100


UPLOAD_FOLDER = 'images'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            getPrediction(filename)
            label, acc = getPrediction(filename)
            flash(label)
            flash(acc)
            flash(filename)
            return redirect('/')

