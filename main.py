from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"
    # return render_template('index.html', name='HS')

@app.route('/hello/<name>')
def hello(name):
    action = request.args.get('action')
    sound = request.args.get('sound')
    return render_template(
        'hello.html', 
        data = {
            "name"   : name, 
            "action" : action, 
            "sound"  : sound
        }
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # get 방식이면 로그인 페이지
        return render_template(
            'login.html'
        )
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return "Success"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template(
            'register.html'
        )
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        print(username, email, phone, password)
        return "Success"

if __name__ == '__main__':
    # app.run()
    app.run(debug=True) # reload 기능