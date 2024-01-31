from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello World!!"
    return "Hello World!! 수정 "

if __name__ == '__main__':
    # app.run()
    app.run(debug=True) # reload 기능