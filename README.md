# AI Document Summarizer

A simple web-based document summarization tool powered by a large language model (LLM). Users can paste text or upload `.txt` files and receive summaries in different styles: brief, detailed, or bullet points.

---

## Features
- Accepts text input via textarea or file upload
- Multiple summarization styles: Brief, Detailed, Bullet Points
- Integration with Hugging Face LLM API (`facebook/bart-large-cnn`)
- Graceful handling of API errors
- Basic input validation
- Clean and simple web interface with loader animation

---

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **API:** Hugging Face Transformers API
- **Libraries:** requests, Flask

---

## Setup Instructions

you can install the requirements:
 pip install -r requirements.txt

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
----
2.Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


3.Install dependencies

pip install flask requests


4.Set your Hugging Face API token

HF_API_TOKEN = "<your_hf_api_token>"


5.Run the Flask app

python app.py


6.Open the app

Navigate to http://127.0.0.1:5000/ in your browser

##Usage:

1.Paste your text in the textarea or upload a .txt file.

2.Select the summary style.

3.Click Summarize 🚀.

4.Wait for the loader and view the summary in the output box.

##Design Decisions

1. Frontend-Backend separation: HTML/CSS handles UI, Flask handles API requests.

2. Modular backend function: summarize_text() allows easy extension to other LLM APIs or styles.

3.Error handling & input validation: Ensures reliable user experience.

4.Scalable UI: Loader and output box handle long texts gracefully.

##Future Improvements

1.Add support for multiple LLM APIs (OpenAI, Anthropic, I used huggingface)

2.Add user authentication for API key management

3.Add summary download/export options

4.Enhance UI with real-time streaming summaries

5.Add Advanced styling options

6.we can add Integration with cloud storage

7.we can Highlighting key sentences

8.add Caching summaries

9.add Sentiment & tone analysis integration

10.add Batch document summarization

11.we can also add Batch document summarization

12.we can make it Mobile-friendly responsive UI

13.we can add text preprocessing options

14.Make bullet points collapsible or expandable for easier reading of large summaries.

15.Summarize text in languages other than English by detecting language and using appropriate models.

16.we can Allow users to select exact word/character count for summaries
