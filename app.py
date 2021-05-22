
from flask import Flask, render_template, request

# Declare the app
app = Flask(__name__)


# start an app route
@app.route('/')
# declare function
def main():
    return render_template('app.html')


# form submission route
@app.route('/send', methods=["POST"])
def send():
    if request.method == 'POST':
        resp = request.form
        # start pulling data from input
        num1 = resp.get('num1')
        num2 = resp.get('num2')
        operation = request.form.get('operation')
    # calculation
        if operation == 'add':
            output = float(num1) + float(num2)
            return render_template('app.html', sum=output)
        elif operation == 'subtract':
            output = float(num1) - float(num2)
            return render_template('app.html', sum=output)
        elif operation == 'multiply':
            output = float(num1) * float(num2)
            return render_template('app.html', sum=output)
        elif operation == 'divide':
            output = float(num1) * float(num2)
            return render_template('app.html', sum=output)
        else:
            return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True)
