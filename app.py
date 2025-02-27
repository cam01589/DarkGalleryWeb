import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('submit.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use PORT or default to 10000
    app.run(host='0.0.0.0', port=port)

