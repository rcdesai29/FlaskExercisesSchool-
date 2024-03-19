from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate')
def calculate():
    number = request.args.get('number', '')
    message = 'No number provided!'
    if number:
        try:
            number = int(number)
            if number % 2 == 0:
                message = f'{number} is even'
            else:
                message = f'{number} is odd'
        except ValueError:
            message = f'{number} is not an integer!'
    return render_template('calculate.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
