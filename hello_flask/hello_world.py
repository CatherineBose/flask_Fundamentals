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

#views or logic to render template 
# localhost:5000/ we will run the following "hello_world" function.
def helloWorld():
  #index.html is stored in template folders :: Dont have to mention .html as only html files are in template 
  return render_template ('index') 

#debugging for development purpose set debug=True 
app.run(debug=True)  




# from flask import Flask 
# from flask import render_template  # Import Flask to allow us to create our app.
# app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
#                          # directly, or importing it as a module.                         
# '''                         # localhost:5000/ we will run the following "hello_world" function.
# def hello_world():
#   return 'Hello World!'  # Return the string 'Hello World!' as a response.
# app.run(debug=True)  