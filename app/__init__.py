from flask import session
from flask import request, render_template, Flask, redirect
from data.data_functions import *
from os import urandom
app = Flask(__name__)
debug = True


def unauthorizedFlow():
    '''
    returns static html for when user accesses site they should not
    '''

    #simply redirects to desired site
    return redirect("/static/unauthorized.html", code=302)

#helper method


def userSignedIn():
    '''
    returns the status of user login
    '''
    return 'username' in session.keys() and session['username']


@app.route("/", methods=['GET', 'POST'])
def welcome():
    '''
    Welcome Page
    '''
    return 'You can do better than this. Go forth!'

@app.route("/login", methods = ['GET','POST'])
def login():
    '''login page'''

    return render_template('login_Page.html')

@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    '''
    register page
    '''
    try:
        if userSignedIn():
            return unauthorizedFlow()

        return render_template('register.html')
    except:
        return render_template('ErrorResponse.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    '''
    logs out the user by setting 'username' key to None
    '''

    try:
        session['username'] = None
        return render_template('login_Page.html', extra_Message="Successfully Logged Out")
    except:
        return render_template('ErrorResponse.html')


def main():
    """
    false if this file imported as module
    debugging enabled
    """
    try:
        app.debug = True
        app.run()
    except:
        return render_template('ErrorResponse.html')


if __name__ == "__main__":
    main()
