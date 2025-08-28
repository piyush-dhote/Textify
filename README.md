# 🔎 Textify - Image to Text Extractor

Textify is a simple and clean web application that allows users to upload an image and extract any text it contains using Optical Character Recognition (OCR).

---
##  🚀 Features

- **Image Upload**: Supports common image formats (.png, .jpg, .jpeg, .gif).
- **Text Extraction**: Uses the Tesseract OCR engine to accurately extract text from images.
- **Modern UI**: A clean, user-friendly interface with a loading indicator during processing.
- **Copy to Clipboard**: Easily copy the extracted text with a single click.
- **Responsive Design**: Works smoothly on both desktop and mobile browsers.

## Tech Stack

| Tool/Library             | Purpose                                       |
|--------------------------|-----------------------------------------------|
| `Backend`                | Python with the Flask framework               |
| `OCR Engine`             | Google's Tesseract OCR                        |
| `pytesseract`            | A Python wrapper for the Tesseract OCR engine |
| `Pillow`                 | An image processing library                   |
| `Frontend`               | HTML5, CSS3 with Bootstrap 4                  |
| `Deployment`             | Hosted on PythonAnywhere                      |

---

## 📦 Setup and Installation
To run this project on your local machine, follow these steps:

### Prerequisites
1. **Python 3**: Make sure you have Python 3 installed.

2. **Tesseract OCR Engine**: You must install the Tesseract engine on your system.

    - **macOS**: ``` brew install tesseract```
    - **Linux (Debian/Ubuntu)**: ```sudo apt install tesseract-ocr```
    - **Windows**: Download and run the installer from the [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) page. 
    
        **Important**: Add the Tesseract installation directory to your system's PATH.

### Installation Steps
```bash
1. Clone the repository:

git clone https://github.com/your-username/Textify.git
cd Textify

2. Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required Python packages:

pip install -r requirements.txt

4. Run the application:

python app.py

5. Open your web browser and navigate to http://127.0.0.1:5000/.
```

---

## Deployment
This application is deployed on PythonAnywhere. The deployment process involves:

1. Pushing the project code to a GitHub repository.
2. Cloning the repository on the PythonAnywhere server.
3. Setting up a new Flask web app and configuring the source code paths.
4. Editing the WSGI configuration file to point to the Flask app instance.
5. Installing dependencies using ```pip install --user -r requirements.txt```.

## Contributing

We welcome contributions! Please feel free to open issues, submit pull requests, or suggest new features.

## License

This project is licensed under the MIT License.