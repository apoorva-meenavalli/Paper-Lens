import fitz  # PyMuPDF
import google.generativeai as genai
from docx import Document
import os
from dotenv import load_dotenv
load_dotenv() 
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"PDF Extraction Error: {e}")
        return None

def extract_text_from_docx(docx_path):
    """Extracts text from a Word .docx file."""
    try:
        doc = Document(docx_path)
        full_text = [para.text for para in doc.paragraphs]
        return "\n".join(full_text)
    except Exception as e:
        print(f"Word Extraction Error: {e}")
        return None

def generate_structured_summary(text):
    """Sends text to PaperLens AI (Gemini) and returns a structured summary."""
    if not text:
        return "Error: No text extracted from the document."

    # Using the working Gemini 2.5 Flash model
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
    You are the PaperLens AI Research Assistant. 
    Analyze the following document and provide a high-quality, professional summary.
    
    Structure the response using these headings:
    ### 1. Objective & Research Question
    ### 2. Methodology & Approach
    ### 3. Key Findings & Results
    ### 4. Significance & Conclusion
    ### 5. Practical Implications
    
    Document Content:
    {text[:20000]}  # Sending first 20k characters to stay within free limits
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Generation Error: {str(e)}"