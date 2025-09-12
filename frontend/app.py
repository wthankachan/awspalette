from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)
@app.route("/")
def customerdata():
    return render_template('customerdata.html')

@app.route("/generate")
def customerprofile():
    return render_template('customerprofile.html')

@app.route("/social")
def socialmedia():
    return render_template('socialmedia.html')
if (__name__== '__main__'): app.run(host='0.0.0.0',port='8080',debug=True)

if (__name__== '__main__'): app.run(host='0.0.0.0',port='8080',debug=True)
