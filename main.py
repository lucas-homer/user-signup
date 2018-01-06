from flask import Flask, request, redirect, render_template
import cgi 
import os



app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args['username']
        
    return render_template('welcome.html', username = username) 


def valid_len(i):
    if len(i) >= 3 and len(i) <= 20 and not ' ' in i:
        return True

    else:
        return False

        

@app.route("/", methods=['POST'])
def validate_signup():
    #encoded_error = request.args.get("error")
    
    username = request.form.get('username')
    password = request.form.get('password')
    verify = request.form.get('verify')
    email = request.form.get('email')
    
    username_error = ''
    password_error = ''
    password_verify_error = ''
    email_error = ''



    if not valid_len(username):
        username_error = 'Please provide a username 3-20 characters long (no spaces)'
        username = ''
    
    if not valid_len(password):
        password_error = 'Please provide a password 3-20 characters long (no spaces)'
        password = ''

    elif password != verify or len(verify) == 0:
        password_verify_error = "Passwords don't match"
        verify = ''

    if len(email) > 0:
        if not valid_len(email):
            email_error = 'Please provide an email 3-20 characters long (no spaces)'
            email = ''
        
        else:
            if not '.' in email and not '@' in email:
                email_error = 'Email address must contain an "@" and a "."'
                email = ''
    

    if not username_error and not password_error and not password_verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, password_verify_error=password_verify_error, email_error=email_error)
    


@app.route('/')
def index():
    return render_template('signup.html')
     

    
if __name__ == '__main__':
    app.run()

# error=encoded_error and cgi.escape(encoded_error, quote=True)
