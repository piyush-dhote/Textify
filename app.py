import os
from flask import Flask, render_template, request, redirect, url_for,flash
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'supersecretkey'

# checking if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower in ALLOWED_EXTENSIONS

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Perform OCR on the uploaded image
            try:
                text = pytesseract.image_to_string(Image.open(filepath))
            except Exception as e:
                flash(f'Error processing image: {e}')
                return redirect(request.url)

            # Render the result template with the extracted text and image filename
            return render_template('result.html', text=text, filename=filename)

    return render_template('index.html')
    
# Route to serve uploaded files
@app.route('/uploads/<filname>')
def uploaded_file(filename):
    # route to display uploaded image on result page 
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# main application 
if __name__ == '__main__':
    # creating upload directory if it doesn't exist 
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
