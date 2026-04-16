from flask import Flask, render_template, request, jsonify
import os
from processor import extract_text_from_pdf, extract_text_from_docx, generate_structured_summary

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        file_extension = os.path.splitext(file.filename)[1].lower()
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # 1. Extract text based on file type
        text = None
        if file_extension == '.pdf':
            text = extract_text_from_pdf(file_path)
        elif file_extension == '.docx':
            text = extract_text_from_docx(file_path)
        
        if not text:
            os.remove(file_path)
            return jsonify({'error': 'Could not read file content'}), 500

        # 2. Generate summary via PaperLens AI
        summary = generate_structured_summary(text)

        # 3. Cleanup: Remove the file after processing
        os.remove(file_path)

        return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)