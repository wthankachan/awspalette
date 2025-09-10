from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)
@app.route("/")
def chatbot():
    return render_template('customerprofile2.html')
if (__name__== '__main__'): app.run(host='0.0.0.0',port='8080',debug=True)