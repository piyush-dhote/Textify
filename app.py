# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract

# Configure the Flask application
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size
app.secret_key = 'supersecretkey'

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            try:
                # --- OPTIMIZATION START ---
                # Open the image file
                img = Image.open(filepath)

                # 1. Convert to grayscale - simplifies the image
                img = img.convert('L')

                # 2. Resize if the image is very large
                MAX_WIDTH = 1600
                if img.width > MAX_WIDTH:
                    scaling_factor = MAX_WIDTH / img.width
                    new_height = int(img.height * scaling_factor)
                    img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)

                # Perform OCR on the pre-processed image
                text = pytesseract.image_to_string(img)
                # --- OPTIMIZATION END ---

            except Exception as e:
                flash(f'Error processing image: {e}')
                return redirect(request.url)
                
            return render_template('result.html', text=text, filename=filename)
    
    return render_template('index.html')

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Main entry point for the application
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
