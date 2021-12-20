from flask import session
from flask import request, render_template, Flask, redirect
from data.data_functions import *
from os import urandom
from data.recipe_data import *
app = Flask(__name__)
debug = True

app.secret_key = urandom(24)

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
    if userSignedIn():
        return "logged in"
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


@app.route("/check_register", methods=['GET', 'POST'])
def check_register():
    '''
    function for post-form request; register process given POST form arguments
    '''

    try:
        if userSignedIn():
            return unauthorizedFlow()

        #store form information
        username = request.form.get('username')
        password = request.form.get('password')
        con_password = request.form.get('confirm_password')

        #checks password requirements against password confirmation and password existence; False means it passes requirements
        password_conflict = (not bool(password)) or password != con_password

        #checks db for existing user and user existence; False means it passes requirements
        username_conflict = (not bool(username)) or user_exists(username)

        if not (password_conflict or username_conflict):
            add_user(username, password)
            return redirect("/login")

        else:
            #Error messages based on incorrect input types
            extra_Message = "An error has been made trying to register you."
            if password_conflict:
                extra_Message = "Password requirements not met. Check to see that password is at least one character and that password confirmation matches"

            elif username_conflict:
                extra_Message = "Username may already be in use, or does not contain at least one character"

            return render_template('register.html', extra_Message=extra_Message)
    except:
        return render_template('ErrorResponse.html')


@app.route("/auth_ed", methods=['POST'])
def authenticate():
    '''
    authorization page; redirects and logs in if credentials work, loads login template if not
    '''
#try:
    #retrieve from FORM instead of ARGS because we are retrieving from POST method
    username = request.form.get('username')
    password = request.form.get('password')

    #authflow variable
    loginAuthorized = user_exists(
        username) and correct_password(username, password)
    print(loginAuthorized)

    if loginAuthorized:
        session['username'] = username
        return redirect("/", code=302)
    else:
        return render_template('login_Page.html', extra_Message="Login failed, please try again")

#except:
    #return render_template('ErrorResponse.html')

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

@app.route("/band/<string:band>")
def get_band(band):
    return redirect("/description/kpop/band/Blackpink")

#attribute,table,search,condition
@app.route("/<string:attribute>/<string:table>/<string:search>/<string:condition>")
def get_info(attribute, table, search, condition):
    return render_template("display_band.html", band=condition, contents=getInformation(attribute, table, search, condition)[0][0])

def main():
    """
    false if this file imported as module
    debugging enabled
    """
    try:
        app.debug = True
        app.run(host="0.0.0.0")
    except:
        return render_template('ErrorResponse.html')


if __name__ == "__main__":
    main()
