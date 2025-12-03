# Story2Comic – AI-Powered Story to Comic Generator

Story2Comic is a Python-based project that converts a short textual story into a black-and-white, manga-style comic page.  
It combines **NLP (spaCy)** for story understanding and **AI image generation (Stable Diffusion)** for creating visual comic panels.

---

## 📌 Project Objective

The main goal of this project is to:
- Take a short story (1–3 paragraphs) as input
- Identify characters, actions, and dialogues
- Generate illustrated comic panels
- Add speech bubbles
- Arrange panels into a complete comic page

This project demonstrates the practical integration of **Natural Language Processing** and **Computer Vision** for creative media generation.

---

## 📁 Folder Structure

```text
Story2Comic-main/
│
├── example/
│   └── example_story.txt          → Sample input story
│
├── outputs/
│   ├── comics/                     → Final generated comic pages
│   └── tmp/                        → Temporary generated panels
│
├── src/
│   ├── assemble.py                 → Combines panels into a comic page
│   ├── bubble_layout.py            → Adds speech bubbles to panels
│   ├── character.py                → Detects and manages character data
│   ├── generate_panel.py           → Generates individual comic panels
│   ├── main.py                      → Main controller file
│   ├── nlp_utils.py                 → NLP processing using spaCy
│   └── utils.py                     → Helper functions
│
├── requirements.txt
├── temp_story.txt
└── README.md
```

---

## ⚙️ Technologies Used

- **Python**
- **spaCy** (NLP for character & context extraction)
- **Stable Diffusion** (AI image generation)
- **Pillow (PIL)** (Image processing & bubbles)
- **PyTorch**
- **NumPy**

---

## 🚀 How to Run the Project

### 1. Setup Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # For Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run with Example Story

```bash
python src/main.py --story example/example_story.txt
```

The output comic page will be saved in:

```
outputs/comics/
```

---

## 🧠 Working of the Project (Flow)

**Step 1: Input Story**  
User provides a short story in text format.

⬇

**Step 2: NLP Processing** (`nlp_utils.py`)  
- Identifies characters
- Extracts actions & dialogues

⬇

**Step 3: Panel Generation** (`generate_panel.py`)  
- Uses Stable Diffusion to generate images for each story scene

⬇

**Step 4: Speech Bubbles** (`bubble_layout.py`)  
- Adds dialogue text in bubble format

⬇

**Step 5: Page Assembly** (`assemble.py`)  
- Combines all panels into one comic page

⬇

✅ **Final Comic Output**

---

## ✅ Example Output

A sample generated image can be found here:

```
outputs/comics/comic_page.png
```

Each panel is first created in:

```
outputs/tmp/
```

---

## 📌 Use Cases

- Comic & manga creators
- Educational storytelling tools
- Entertainment applications
- NLP + CV academic projects
- AI art generation demos

---

## ⚠️ Notes

- For best results, use short stories (100–300 words)
- A GPU is recommended for faster image generation
- Large stories may take longer to process
- Results improve with clearer character descriptions

---

## 🌟 Future Improvements

- Add color comic support
- Web interface (using Streamlit/Flask)
- Multiple comic pages
- Different art styles (cartoon, anime, realistic)
- Voice narration

---

## 👨‍🎓 Made for Academic & Project Use

This project is suitable for:
- AI / ML Mini Project
- Computer Vision Project
- NLP Integration Work
- Final Year Project Demo

---

Feel free to modify and enhance this for your own needs.
