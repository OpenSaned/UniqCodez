from flask import Flask, request, render_template
from time import time
import os
import requests

logger = os.environ.get('LOG_SERVER')
app = Flask(__name__)
def convertToBinary(int):
    num = bin(int).replace("0b", "")
    if len(num) < 8:
        ext = "0" *(8 - len(num))
        num = ext + num
    return num.replace('1','▀').replace('0','▄')

@app.route('/tweet', methods=['POST'])
def tweet():
    print(request.data.decode() == "")
    ip = request.headers['X-Forwarded-For'] # change to ip = request.remote_addr for local hosting
    requests.get(url=f"{logger}/tweet", data=ip)
    return "OK"
    
@app.route('/')
def index():
    ip = request.headers['X-Forwarded-For'] # change to ip = request.remote_addr for local hosting
    print("Got request from " + ip)
    code=[]
    for i in ip.split('.'):
        code.append(convertToBinary(int(i)))
    requests.get(url=f'{logger}/http', data=ip)
    return render_template("index.html", code=code, host=request.host_url, logger=logger)

# @app.route("/http"):
# def http():
#     ip = request.headers['X-Forwarded-For'] # change to ip = request.headers['X-Forwarded-For'] for local hosting
#     with open("http.log", a) as file:
        

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
