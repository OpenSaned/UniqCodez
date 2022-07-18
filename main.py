from flask import Flask, request, render_template
from time import time

app = Flask(__name__)

def convertToBinary(int):
    num = bin(int).replace("0b", "")
    if len(num) < 8:
        ext = "0" *(8 - len(num))
        num = ext + num
    return num.replace('1','▀').replace('0','▄')

def getTweet(code):
    out = ""

@app.route('/tweet')
def tweet():
    ip = request.remote_addr
    with open("tweet.log", 'a') as file:
        file.write(f"{time()} - {ip}\n")
    
@app.route('/')
def index():
    ip = request.remote_addr
    code=[]
    for i in ip.split('.'):
        code.append(convertToBinary(int(i)))
    with open("http.log", 'a') as file:
        file.write(f"{time()} - {ip}\n")
    return render_template("index.html", code=code, host=request.host_url)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
