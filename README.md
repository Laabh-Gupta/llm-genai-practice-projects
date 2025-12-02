# 📌 Overview #

This repository is a consolidated collection of my LLM and Generative AI practice projects, experiments, and study notebooks.
It brings together all the small applications, demos, exploratory notebooks, and learning-based implementations I built while studying:

Large Language Models (LLMs)

Prompt Engineering

Embeddings & Vector Databases

Text Classification & Summarization

PDF/Document Parsing

Conversational AI

RAG (Retrieval-Augmented Generation) pipelines

NLP fundamentals

The purpose of this repo is to maintain a single organized place for all GenAI mini-projects I completed during my learning phase.
Each folder contains a self-contained project with its own scripts, sample inputs, and requirements.txt, ranging from simple chatbots to data extraction tools.

While these are not production-grade applications, they demonstrate:

My understanding of LLM workflows

Hands-on projects across multiple domains

Usage of OpenAI, Hugging Face, and classical ML models

Real-world document processing and automation tasks

Experimentation with conversational AI and text generation

This repo acts as both:

A knowledge base of everything I studied (ML, NLP, GenAI), and

A personal practice lab where I experimented with multiple frameworks to strengthen my skills.

It includes various LLM-powered tools such as:

ChatGPT-like interfaces

MCQ generators

Resume screeners

Email and marketing content generators

PDF invoice extractors

Customer-care call summarizers

Support chatbots

Code reviewers

CSV/Document analysis apps

Each project section below explains:

What the app does

Which libraries or APIs it uses (OpenAI, HF Transformers, etc.)

Input and output formats

How to run it

Environment variables required

This repository reflects my journey in learning and applying Machine Learning → NLP → LLMs → GenAI applications through hands-on practice.

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
**About:** Educational notebook covering LLM basics (embeddings, transformers, attention). Open and read for theory & examples. citeturn1view0  
**How to run:** Open in Jupyter; ensure that cells with API tokens are removed or converted to use environment variables.

---

## Repository-wide instructions

### 1) Secrets & `.env`
- **Never commit** `.env` files with real API keys. Keep `*.env` in `.gitignore`. Use `.env.example` with placeholders instead.  
- Regenerate any keys that were previously committed to this repo (you may have already done this).

### 2) Git LFS / Large files
- If you have large model files, Jupyter checkpoints, or audio files, use **Git LFS** or remove them from git and use release assets or external storage.  
  Example: `git lfs install` and `git lfs track "*.mp3"`

### 3) `.gitignore` template (recommended)
```
# env
.env
*.env

# Python
__pycache__/
*.pyc
.ipynb_checkpoints/

# Data
*.csv
*.db
*.sqlite3

# Virtual envs
venv/
.env/
```

### 4) How to run locally (example)
```bash
# clone repo
git clone https://github.com/Laabh-Gupta/llm-genai-practice-projects.git
cd llm-genai-practice-projects

# per-project: follow the project's README / requirements.txt
pip install -r "ChatGPT Clone/requirements.txt"
# then run the app or notebook
python "ChatGPT Clone/app.py"
```

---

## Final notes & next steps (recommended edits I can make)
1. I can **auto-generate per-project README.md files** inside each folder (short and precise) if you want — I’ll populate the fields with info extracted from each `requirements.txt`, `app.py`, and notebooks.  
2. I can **scan your notebooks and code to remove any remaining secrets** and produce a clean commit.  
3. I can create a `portfolio` README that links to the *best 3 projects* and shows screenshots + short demos for placement use.

If you want me to do (1) or (2), say **“Scan & generate per-project READMEs”** or **“Scan & clean secrets”** — I’ll run a focused pass.

---

**Generated by ChatGPT — repository scan referenced:** citeturn0view0
