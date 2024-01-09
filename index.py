from flask import Flask, request, render_template
from time import time
import os
import requests

app = Flask(__name__)
def convertToBinary(int):
    num = bin(int).replace("0b", "")
    if len(num) < 8:
        ext = "0" *(8 - len(num))
        num = ext + num
    return num.replace('1','▀').replace('0','▄')

@app.route('/tweet', methods=['POST'])
def tweet():
    ip = request.remote_addr 
    with open("tweet.log", "a") as f:
        f.write(f"{ip} - {time()}\n") 
    return "200 OK"
    
@app.route('/')
def index():
    ip = request.remote_addr
    code=[]
    for i in ip.split('.'):
        code.append(convertToBinary(int(i)))
    with open("http.log", "a") as f:
        f.write(f"{ip} - {time()}\n")
    return render_template("index.html", code=code, host="uniqcodez.vercel.app")
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)  
