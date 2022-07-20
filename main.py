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

@app.route('/tweet')
def tweet():
    ip = request.remote_addr
    requests.get(url=f"{logger}/tweet")
    
@app.route('/')
def index():
    ip = request.remote_addr
    code=[]
    for i in ip.split('.'):
        code.append(convertToBinary(int(i)))
    requests.get(url=f'{logger}/', params={ip})
    return render_template("index.html", code=code, host=request.host_url, logger=logger)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
