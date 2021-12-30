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
        return "logged in users should see something different"
    return render_template("main_page.html")

@app.route("/login", methods = ['GET','POST'])
def login():
    '''login page'''
    if userSignedIn():
        return redirect("/")
    return render_template('login_Page.html')

@app.route("/auth_ed", methods=['POST'])
def authenticate():
    '''
    authorization page; redirects and logs in if credentials work, loads login template if not
    '''
#try:
    #retrieve from FORM instead of ARGS because we are retrieving from POST method
    if userSignedIn():
        return redirect("/")
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


#attribute,table,search,condition
@app.route("/<string:attribute>/<string:table>/<string:search>/<string:condition>")
def get_info(attribute, table, search, condition):
    return render_template("display_band.html", band=condition, contents=getInformation(attribute, table, search, condition)[0][0])


@app.route("/table", methods=['GET', 'POST'])
def table():
    response = request.args.get("query")
    response = getMatches("contacts", "first_name", response)


    return render_template("search_table.html",response=response)

@app.route("/members",methods=['GET'])
def members():
    response = ["a","b","c"]
    return render_template("show_list.html",resource_response=response)

@app.route("/searchbar",methods=['GET', 'POST'])
def searchbar():
    if "query" in request.args.keys():
        response = request.args.get("query")
        response = getMatches("contacts", "first_name", response)

        return render_template("searchbar.html", response=response)
    return render_template("searchbar.html")

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
