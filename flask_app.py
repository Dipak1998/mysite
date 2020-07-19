from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/<string:page>')
def send_template(page):
    return render_template(page)

if __name__ == "__main__":  
    app.run(port=3000, debug=True)