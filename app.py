from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        image.save(f"uploads/{image.filename}")  # Save uploaded image
        return "Image uploaded successfully!"
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)

