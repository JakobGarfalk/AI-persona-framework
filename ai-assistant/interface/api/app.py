from flask import Flask, url_for
from routes import UrlFn_Index, UrlFn_Selector

# Flask constructor takes the name of 
# current module (__name__) as argument.
SERVER_NAME = "Flask-Interface"
App = Flask(__name__)

App.url_for("/", UrlFn_Index)
App.url_for("/select", UrlFn_Selector)

App.run(host="0.0.0.0", port=8000)

# main driver function
#if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    #App.run(host="0.0.0.0", port=8000)