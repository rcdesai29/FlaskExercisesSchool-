from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will act as a simple database for this example
registered_users = {}

# A list of allowed organizations
allowed_organizations = [
    'Student Council',
    'Debate Club',
    'Chess Club',
    'Science Club',
    'Math Society'
]

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']

        # Backend validation
        if not name or organization not in allowed_organizations:
            error = 'Invalid name or organization'
        else:
            registered_users[name] = organization
            return redirect(url_for('users'))

    return render_template('home.html', error=error, organizations=allowed_organizations)

@app.route('/users')
def users():
    return render_template('users.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
