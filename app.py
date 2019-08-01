from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template("index.html")

#@app.route('/about')
#def index():
#    return render_template("about.html")
if __name__ == '__main__':
   #app.run()
   #app.debug = True
   #app.run()
   app.run(debug=True,host='0.0.0.0')
