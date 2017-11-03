from flask import Flask
from flask import render_template
# End of imports 
app = Flask(__name__)
'''
Global variable __name__ tells Flask whether or not we are running the file
 directly, or importing it as a module.
'''

#Route '/' home route 
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/projects')
def projectsPage():
    return render_template('projects.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')

app.run(debug=True) 
