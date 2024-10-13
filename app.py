from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    name = request.form['name']
    message = request.form['message']
    number = request.form['number']
    email = request.form['email']

    return render_template('result.html', name=name, message=message,number=number,email=email)


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=3654)