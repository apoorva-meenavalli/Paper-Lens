# Paper Lens: AI-Driven Research Paper Summarizer

Paper Lens is a robust document processing application designed to streamline academic literature reviews. It automates the extraction of unstructured text from complex PDF and Word documents and transforms them into structured, actionable insights.

## 🚀 Key Features
* **Multi-Format Support:** Seamlessly processes both `.pdf` and `.docx` research papers.
* **Structured Analysis:** Generates summaries categorized by *Objectives*, *Methodology*, *Key Findings*, and *Conclusion*.
* **Secure Architecture:** Implements environment variable management to protect sensitive API credentials.
* **Clean UI:** A minimalist, user-friendly Flask web interface for document uploads.

## 🛠️ Technical Stack
* **Backend:** Python, Flask
* **Document Parsing:** PyMuPDF (fitz), python-docx
* **LLM Integration:** Google Gemini 1.5 Flash API
* **Environment Management:** python-dotenv
