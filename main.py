from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

















'''
@app.route("/welcome", method=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        username = request.form('username')

        return render_template('welcome.html', username=username)
'''


@app.route("/", methods=['POST', 'GET'])
def index():
    #encoded_error = request.args.get("error")
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()

# error=encoded_error and cgi.escape(encoded_error, quote=True)