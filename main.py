from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True
def at_sign(string):
    for letter in string:
        if letter == '@':
            return True
    return False
def period(string):
    for letter in string:
        if letter == '.':
            return True
    return False
def has_space(string):
    for letter in string:
        if letter == ' ':
            return True
    return False
def length(string):
    if len(string) > 2 and len(string) < 21:
        return True
    else:
        return False


@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    pw1 = request.form['pw1']
    pw2 = request.form['pw2']
    email = request.form['email']
    
    username_error = ''
    pw1_error = ''
    pw2_error = ''
    email_error = ''

    if not username:
        username_error = 'Please enter a username'
    if not pw1:
        pw1_error = 'Please enter a password'
    if not pw2:
        pw2_error = 'Please verify your password'
    if has_space(username):
        username_error = 'Username cannot contain space'
    if has_space(pw1):
        pw1_error = "Password cannot contain space"
    if not length(username):
        username_error = 'Username must be three to twenty characters long'
    if not length(pw1):
        pw1_error = "Password must be three to twenty characters long"
    if pw1 != pw2:
        pw2_error = 'Passwords do not match'
    if not at_sign(email):
        email_error = 'E-mail must contain one "@" sign'
    if not period(email):
        email_error = 'E-mail must contain one "."'
    if not length(email):
        email_error = "E-mail must be three to twenty characters long"
    
    if not username_error and not pw1_error and not pw2_error and not email_error:
        return redirect('/welcome?user={0}'.format(username))
    else:
        return render_template('index.html', title='Signup', username=username, email=email,username_error=username_error, pw1_error=pw1_error, pw2_error=pw2_error, email_error=email_error)
    

@app.route('/welcome')
def welcome():
    username = request.args.get('user')
    return render_template('welcome.html', title="Welcome", username=username)

@app.route("/")
def signup():
    return render_template("index.html", title="Signup")

app.run ()

