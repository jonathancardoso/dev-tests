from werkzeug.utils import secure_filename
from sqlalchemy.orm import sessionmaker
from tabledef import *
import json
import os

#env variables
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
engine = create_engine('sqlite:///testedevpython.db', echo=False)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def auth(user,password):
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([user]), User.password.in_([password]) )
    result = query.first()
    s.close()
    return result

def upload(request):
    # check if the post request has the file part
    if 'file' not in request.files:
        e = 'No file part'
        return json.dumps({'status':'error','message':e})

    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        e = 'No selected file'
        return json.dumps({'status':'error','message':e})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        e = 'File successfully uploaded'
        fullpath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(fullpath)
        return json.dumps({'status':'ok','path':fullpath})
