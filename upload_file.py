import os
from flask import Flask, request
from werkzeug.utils import secure_filename    # 获取上传文件的文件名

UPLOAD_FOLDER = '/home/shiyanlou/Code'    # 上传路径
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])    # 允许上传的文件类型

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):    # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，
                              # 两者 都满足则返回 true
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS # rsplit('.',分割次数)，分割1次，2个中取第二个即[1]

@app.route('/',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':    # 如果是POST请求方式
        f = request.files['file']    # 获取上传的文件
        if f and allowed_file(f.filename):    # 如果文件存在并且符合要求则为true
            fname = secure_filename(f.filename)    # 获取上传文件的文件名
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))    # 保存文件
            return '{} upload successed!'.format(fname)    # 返回保存成功的信息
    # 使用 GET 方式请求页面时 或 上传文件失败时 返回上传文件的表单页
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
