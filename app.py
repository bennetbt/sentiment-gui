from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# this ('/') route you can rename to the route you want, thats what accesses the login route
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # your replace the email and password with the values you want
    if email == 'example@example.com' and password == 'password123':
        # after login the user is redirected to the success route so change the route name to what you want if dashboard or any thing
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

 
# this is the success route so change the route name to what you want or the page you want the user to access after login
@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)
