from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def password_generator():
    password = ''
    length = 0
    if request.method == 'POST':
        length = request.form.get('length')
        length = int(length)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)
