from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form.get('length', 12))
    use_lowercase = 'lowercase' in request.form
    use_uppercase = 'uppercase' in request.form
    use_digits = 'digits' in request.form
    use_special_chars = 'special_chars' in request.form

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character set."

    password = ''.join(random.choice(characters) for _ in range(length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=False)
