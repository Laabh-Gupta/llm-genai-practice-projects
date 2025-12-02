# 📌 Overview

This repository is a consolidated collection of my LLM and Generative AI practice projects, experiments, and study notebooks.  
It brings together all the small applications, demos, exploratory notebooks, and learning-based implementations I built while studying:

- **Large Language Models (LLMs)**
- **Prompt Engineering**
- **Embeddings & Vector Databases**
- **Text Classification & Summarization**
- **PDF/Document Parsing**
- **Conversational AI**
- **RAG (Retrieval-Augmented Generation) pipelines**
- **NLP fundamentals**

The purpose of this repo is to maintain a single organized place for all GenAI mini-projects I completed during my learning phase.  
Each folder contains a self-contained project with its own scripts, sample inputs, and `requirements.txt`, ranging from simple chatbots to data extraction tools.

While these are not production-grade applications, they demonstrate:

- My understanding of LLM workflows  
- Hands-on projects across multiple domains  
- Usage of OpenAI, Hugging Face, and classical ML models  
- Real-world document processing and automation tasks  
- Experimentation with conversational AI and text generation  

This repo acts as both:

- A knowledge base of everything I studied (ML, NLP, GenAI), and  
- A personal practice lab where I experimented with multiple frameworks to strengthen my skills.

It includes various LLM-powered tools such as:

- ChatGPT-like interfaces  
- MCQ generators  
- Resume screeners  
- Email and marketing content generators  
- PDF invoice extractors  
- Customer-care call summarizers  
- Support chatbots  
- Code reviewers  
- CSV/Document analysis apps  

Each project section below explains:

- What the app does  
- Which libraries or APIs it uses (OpenAI, HF Transformers, etc.)  
- Input and output formats  
- How to run it  
- Environment variables required  

This repository reflects my journey in learning and applying **Machine Learning → NLP → LLMs → GenAI** applications through hands-on practice.

---

### Automatic Ticket Classification Tool
**About:** Small demo that classifies support tickets (e.g., HR, IT, Transport) into categories and can create a simple ML model for routing tickets.  
**Resources used:** `scikit-learn` (likely), pandas, basic ML models (SVM/logistic regression). Replace with actual libs used in `/Automatic Ticket Classification Tool/requirements.txt`.  
**Input format:** CSV (e.g. `Tickets.csv`) — raw ticket text and optional metadata.  
**Output format:** CSV with predicted labels or a persisted model file (e.g., `modelsvm.pk1`).  
**How to run:** (example)
```bash
cd "Automatic Ticket Classification Tool"
pip install -r requirements.txt
python app.py
```
**Env vars:** None expected (remove any hard-coded keys).  
**Notes:** Move large binary model files out of git (use releases or artifact storage).

---

### CSV Data Analysis
**About:** Notebook / script for analyzing tabular CSV data (employees example included).  
**Resources used:** pandas, matplotlib, Jupyter. Check `requirements.txt`.  
**Input format:** CSV files under repository (`employees.csv`).  
**Output format:** Plots, processed CSV outputs.  
**How to run:** Open the Jupyter notebook or run `python app.py`.  
**Env vars:** None expected.

---

### ChatGPT Clone
**About:** Small demo to mirror a chat interface that uses LLM APIs for responses. Intended as a learning demo for prompt flow and web UI integration.  
**Resources used (likely):** OpenAI API (or other LLM provider), Flask/Streamlit/FastAPI (check `requirements.txt`).  
**Input format:** User text input via UI or REST.  
**Output format:** Text responses in chat format.  
**How to run:** Refer to the folder `ChatGPT Clone/requirements.txt` and `app.py`.
**Env vars:** `OPENAI_API_KEY` (use environment variables, not hard-coded).

---

### Code Review Analyst App
**About:** Tool that ingests PR diffs or code files and produces review-style comments or suggestions (LLM-assisted).  
**Resources used:** OpenAI / HuggingFace, Python libraries. Check `app.py`.  
**Input format:** Source code files or text diffs.  
**Output format:** Structured review text or JSON.  
**How to run:** `python app.py` after installing `requirements.txt`.  
**Env vars:** `OPENAI_API_KEY` or equivalent.

---

### Customer Care Call Summary Alert
**About:** Summarizes audio call recordings to generate short summaries or alerts. Useful for contact center automation experiments.  
**Resources used:** Speech-to-text libraries (e.g., OpenAI Whisper, HuggingFace ASR, or speech SDKs), NLP summarization (LLMs). Check `requirements.txt`.  
**Input format:** `.mp3` recordings under `Call Recordings/`.  
**Output format:** Text summaries (plain text or CSV).  
**How to run:** `python app.py` (see utils.py).  
**Env vars:** Any cloud keys for speech APIs—remove before committing.

---

### Data Connections
**About:** Notebook showing sample data connections / quickstarts.  
**Resources used:** Jupyter, connectors; see the notebook.  
**Input format:** Small sample `.txt` or other connectors.  
**Output format:** Notebook outputs & visualizations.  
**How to run:** Open `Data Connections/Data Connections - Overview.ipynb` in Jupyter.  

---

### Email Generator App
**About:** Generates email drafts using prompts or templates (LLM-assisted).  
**Resources used:** OpenAI / LLM provider. Check `requirements.txt`.  
**Input format:** Prompt / form fields (recipient, subject, tone).  
**Output format:** Email text.  
**How to run:** `python app.py`.

---

### Invoice Extraction Bot
**About:** Parses invoices (PDFs) to extract structured fields (ID, totals, dates). Useful for information extraction experiments.  
**Resources used:** PDF parsing libs (`pdfplumber`/`PyPDF2`), OCR, LLMs for post-processing.  
**Input format:** PDFs in `Invoice/` folder.  
**Output format:** JSON/CSV of extracted fields.  
**How to run:** `python app.py`.

---

### Let's Build Simple Conversational Application
**About:** Guided demo that builds a conversational app (probably from a course).  
**Resources used:** HuggingFace or OpenAI, small Flask/Streamlit app. See `app.py` and `env-sample.txt`.  
**Input format:** User chat input.  
**Output format:** Chat responses.  
**How to run:** Follow `env-sample.txt` and `requirements.txt`.

---

### Let's build Similar Words Finder Application
**About:** Finds similar words or synonyms using embeddings or semantic search.  
**Resources used:** HuggingFace embeddings / spaCy / gensim.  
**Input format:** Single word or list.  
**Output format:** Ranked similar words.

---

### Lets' Build Simple Question Answering Application
**About:** A small extractive QA demo on supplied docs.  
**Resources used:** HuggingFace / OpenAI, vector DB optional.  
**Input format:** Query string + supporting docs.  
**Output format:** Answer text + source snippets.  
**How to run:** Check `app.py` and `env-sample.txt` for required model keys.

---

### MCQ Creator App
**About:** Notebook-based project to generate MCQs from input documents using LLMs.  
**Resources used:** Likely OpenAI or HF (notebook cells may contain API tokens — verify and remove). See `MCQ Creator App/MCQ Creator.ipynb`. citeturn0view0  
**Input format:** PDF/DOCX or plain text.  
**Output format:** Structured MCQs with options/answers.  
**How to run:** Open the notebook and run cells; install `requirements.txt` if present.  
**Env vars:** `OPENAI_API_KEY` or `HF_TOKEN` — **do not commit these**.

---

### Marketing Campaign App - Project Source Code
**About:** Demo to generate marketing content (emails/posts) based on prompts.  
**Resources used:** LLM provider; see `.env.example` and `app.py`.  
**Input format:** Product brief or bullet points.  
**Output format:** Marketing copy outputs.

---

### Resume Screening Assistance Project
**About:** Uses NLP/LLMs to score or classify resumes against job descriptions.  
**Resources used:** Possibly HuggingFace / OpenAI + classic NLP libs (spaCy). Check `requirements.txt`.  
**Input format:** Resume files inside `Docs/`.  
**Output format:** Scores, shortlisted candidates, CSV outputs.  
**How to run:** `python app.py` after installing requirements.  
**Env vars:** `OPENAI_API_KEY` or similar — ensure removed from files.

---

### Support Chat Bot For Your Website
**About:** Simple website-support chat widget + backend using an LLM for responses.  
**Resources used:** OpenAI or HF, web framework, small utils module.  
**Input format:** Web chat form.  
**Output format:** Chat messages; maybe logs.  
**How to run:** `python app.py`.

---

### Youtube Script Writing Tool
**About:** Generates YouTube script ideas and drafts from prompts.  
**Resources used:** LLM provider.  
**Input format:** Prompt / topic.  
**Output format:** Script text files.

---

### LLM Intro.ipynb
**About:** Educational notebook covering LLM basics (embeddings, transformers, attention). Open and read for theory & examples. Covers basics of how to use API Tokens and how to run an LLM Model

---

## 🛠 Repository-wide Instructions (From My Perspective)

### 1) 🔐 Secrets & `.env` Handling  
Throughout all my projects in this repository, I use the pattern:

```
token = "***"
```

This is a **placeholder only**.  
You must **replace `***` with your actual API key** before running any project.

#### Supported keys include:
- **OPENAI_API_KEY**
- **HUGGINGFACE_API_KEY**
- **COHERE_API_KEY** (if used)
- **GROQ_API_KEY** (optional)
- **PINECONE_API_KEY** (for vector DB projects)
- **LANGCHAIN_API_KEY** (if applicable)

#### Important:
- I **never commit real keys** to GitHub.  
- All real API keys should be placed in your local `.env` file such as:

```
OPENAI_API_KEY=your_openai_key
HUGGINGFACE_API_KEY=your_hf_key
PINECONE_API_KEY=your_pinecone_key
```

- Use `.env.example` as the correct reference format.


### 2) 📦 Git LFS for Large Files  
Some projects contain PDFs, MP3s, or model files.  
If you want to modify or add more large files, use **Git LFS**:

```bash
git lfs install
git lfs track "*.mp3"
git lfs track "*.pdf"
git add .gitattributes
```

This keeps the repo fast and clean.


### 3) 🧹 Recommended `.gitignore`

```
# Environment files
.env
*.env

# Python cache
__pycache__/
*.pyc
.ipynb_checkpoints/

# Data
*.db
*.sqlite3

# Virtual environments
venv/
.env/
```

If you add new large model files, also ignore them or use Git LFS.


### 4) ▶️ How to Run Any Project Locally  

Each project in this repo is **self-contained**, so follow these steps:

#### **Clone the repo**
```bash
git clone https://github.com/Laabh-Gupta/llm-genai-practice-projects.git
cd llm-genai-practice-projects
```

#### **Install project-specific dependencies**
Every folder has its own `requirements.txt`.  
Example:

```bash
pip install -r "ChatGPT Clone/requirements.txt"
```

#### **Set up `.env` file**
Create a `.env`:

```
OPENAI_API_KEY=your_key_here
HUGGINGFACE_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
token="your_key_here"   # if the script expects token = "***"
```

> ⚠️ **Note:** Many of my demo apps originally used  
> `token = "***"` inside the code. Replace it locally with your actual key.

### 5) 🚀 Running Specific Frameworks

#### 🟦 **Running Streamlit Apps**
Some projects (e.g., “MCQ Creator App”, “Resume Screening Tool”, etc.) use Streamlit:

```bash
streamlit run app.py
```

#### 🟨 **Running Python Scripts**
Many folders contain a simple `app.py`:

```bash
python app.py
```

#### 🟧 **Running Notebooks**
Open notebooks via:

```bash
jupyter notebook
```
or  
```
jupyter lab
```

#### 🟪 **Using Hugging Face**
If the project loads HF models:

```python
from transformers import AutoModel, AutoTokenizer
token = "***"  # replace with your HF key
```

Or set globally:

```
HUGGINGFACE_API_KEY=your_key_here
```

#### 🟩 **Using Pinecone (Vector DB)**
If the project uses Pinecone for embeddings:

```python
from pinecone import Pinecone
pc = Pinecone(api_key="your_key_here")
```


### 6) 📄 Input / Output Formats (General)

Most projects follow these formats:

#### **Input**
- text (prompt, question, resume, document)
- PDFs (invoice, resume)
- CSV (ticket classification, employee data)
- Audio (`.mp3`) for summarization projects

#### **Output**
- generated text  
- structured JSON  
- CSV with extracted information  
- chat-style responses  
- MCQs or summaries


### 7) 🧪 Notes About This Repo

- This is **not** a production repository.  
- It is my **learning lab** containing:
  - LLM experiments  
  - mini-projects  
  - notebooks  
  - demos  
  - practice code  

- Good for interview explanations:  
  - prompt engineering  
  - embeddings  
  - vector DBs  
  - conversational agents  
  - document parsing  
  - generation tasks  

