from flask import Flask, request, Response
import time
from flask import Flask, flash, request, redirect, url_for, render_template
PATH_TO_TEST_IMAGES_DIR = './images'
import os
import glob
#import face_recognition as face_rec
import shutil
path = 'employee images'
employeeImg = []
employeeName = []
myList = os.listdir(path)
filename = 'click'

app = Flask(__name__)
app.secret_key = "secret key"











@app.route('/')
def index():
    return render_template('index.html')

# save the image as a picture
@app.route('/image', methods=['POST','GET'])
def image():

    filist = (os.listdir('images'))
    for fill in filist:
         os.remove(f'images/{fill}')
        


    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))



    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
