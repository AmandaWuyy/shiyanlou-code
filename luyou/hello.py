from flask import Flask, render_template
app = Flask(__name__)

# 如果访问 /，返回 Index Page
@app.route('/')
def indax():
    return 'Index Page'

# 如果访问 /hello，返回 Hello, World!
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户“id”的结果，注意“int”是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/之后的路径名
    return 'Subpath {}'.format(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()    # 如果是 POST 方法就执行登录操作
    else:
        show_the_login_form()    # 如果是GET方法就展示登录表单



