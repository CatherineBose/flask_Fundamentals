from flask import Flask
from flask import render_template
 
app = Flask(__name__)

@app.route('/')
def homepage():
 return render_template('index.html')

@app.route('/<ninja>')
def ninja(ninja):
    if ninja == 'blue':
        ninjaName = 'leonardo'
    elif ninja == 'orange':
        ninjaName = 'michelangelo'
    elif ninja == 'red':
        ninjaName = 'raphael'
    elif ninja == 'purple':
        ninjaName = 'donatello'
    else:
        ninjaName = 'notapril'
    return render_template('ninja.html', ninja = ninjaName)


app.run(debug=True)