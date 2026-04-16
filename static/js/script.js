const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileNameDisplay = document.getElementById('fileName');
const uploadForm = document.getElementById('uploadForm');
const summarizeBtn = document.getElementById('summarizeBtn');
const loader = document.getElementById('loader');
const resultContainer = document.getElementById('resultContainer');
const summaryContent = document.getElementById('summaryContent');

// Handle Click to Upload
dropZone.addEventListener('click', () => fileInput.click());

// Show selected filename
fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        fileNameDisplay.innerText = fileInput.files[0].name;
        fileNameDisplay.classList.remove('hidden');
    }
});

// Handle Form Submission
uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    if (!fileInput.files[0]) {
        alert("Please select a PDF file first!");
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // UI Transitions
    summarizeBtn.disabled = true;
    loader.classList.remove('hidden');
    resultContainer.classList.add('hidden');

    try {
        const response = await fetch('/summarize', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            alert("Error: " + data.error);
        } else {
            // Render the Markdown/Text from Gemini
            summaryContent.innerHTML = formatSummary(data.summary);
            resultContainer.classList.remove('hidden');
            resultContainer.scrollIntoView({ behavior: 'smooth' });
        }
    } catch (err) {
        alert("An error occurred while connecting to the server.");
    } finally {
        loader.classList.add('hidden');
        summarizeBtn.disabled = false;
    }
});

// Simple function to convert Gemini's Markdown stars to HTML
function formatSummary(text) {
    return text
        .replace(/### (.*)/g, '<h3 class="text-xl font-bold text-indigo-700 mt-4 mb-2">$1</h3>')
        .replace(/\*\* (.*)/g, '<li class="ml-4 list-disc text-slate-700">$1</li>')
        .replace(/\*\*(.*?)\*\*/g, '<strong class="text-slate-900 font-semibold">$1</strong>')
        .replace(/\n/g, '<br>');
}