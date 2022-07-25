from flask import Flask, request, Response
import time
from flask import Flask, flash, request, redirect, url_for, render_template
PATH_TO_TEST_IMAGES_DIR = './images'
import os
import glob
import face_recognition as face_rec
import cv2
import shutil
path = 'employee images'
employeeImg = []

employeeName = []
myList = os.listdir(path)
filename = 'click'

app = Flask(__name__)
app.secret_key = "secret key"

def resize(img, size) :
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)



def findEncoding(images) :
    imgEncodings = []
    for img in images :
        img = resize(img, 0.50)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeimg = face_rec.face_encodings(img)[0]
        imgEncodings.append(encodeimg)
    return imgEncodings
def MarkAttendence(name):
    with open('attendence.csv', 'r+') as f:
        myDatalist =  f.readlines()
        nameList = []
        for line in myDatalist :
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            timestr = now.strftime('%H:%M')
            f.writelines(f'\n{name}, {timestr}')
            statment = str('welcome to seasia' + name)

for cl in myList :
    curimg = cv2.imread(f'{path}/{cl}')
    employeeImg.append(curimg)
    employeeName.append(os.path.splitext(cl)[0])

EncodeList = findEncoding(employeeImg)











@app.route('/')
def index():
    return render_template('index.html')

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():
    print('clicke')

    filist = (os.listdir('images'))
    for fill in filist:
         os.remove(f'images/{fill}')
        


    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))

    print(filename)
    file = (os.listdir('images'))[0]
    
    #frame = load_img('images/'+file, target_size=(224, 224))
    frame = face_rec.load_image_file('images/'+filename)

    #frame = img_to_array(frame)


    facesInFrame = face_rec.face_locations(frame)
    encodeFacesInFrame = face_rec.face_encodings(frame, facesInFrame)
    filist = (os.listdir('images'))
    for fill in filist:
         os.remove(f'images/{fill}')    

    for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame) :
        matches = face_rec.compare_faces(EncodeList, encodeFace)
        facedis = face_rec.face_distance(EncodeList, encodeFace)
        print(facedis)
        if min(facedis) < 100:
            matchIndex = np.argmin(facedis)

            print(matchIndex)
            print(name)

            name = employeeName[matchIndex].upper()
            

            #MarkAttendence(name)
            

    flash(filename)


    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
