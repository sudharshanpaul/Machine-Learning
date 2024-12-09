from flask import Flask

'''
It creates an instance of the flask class,
which will be your WSGI (web server gateway interface) application.
'''

#WSGI application
app = Flask(__name__)  # Her the parameter is the entry point of the application

## If we say..,  google.com is the home page of the specific application
# for making home page we use /

@app.route("/") # / is a decorator ..if we go to the route it will go and call the below function i.e welcome
def welcome():
    return "Hii this is Sudharshan Paul. For complete Machine Learning notes visit www.github.com/sudhaarshanpaul"

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__ == "__main__":
    app.run(debug=True)