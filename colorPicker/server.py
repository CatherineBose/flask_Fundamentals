from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')         
def home_page():
  return render_template('index.html')  

@app.route('/colorPicker', methods=['POST'])
def create():
# notice how the key we are using to access the info corresponds with the colors
# of the inputs from our html form
    r = request.form['red']
    b = request.form['blue']
    g = request.form['green']
    return render_template('colors.html', r = r, g = g, b = b) # redirects back to the '/' route


app.run(debug=True)
