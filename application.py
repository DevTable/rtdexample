from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<img src="/static/quay-logo.png"><br><br>Hello World with static resource!!'

if __name__ == '__main__':
    print 'Starting HTTP server'
    app.run(port=80, debug=True, host='0.0.0.0')
