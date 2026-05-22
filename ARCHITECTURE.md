"""
🚀 SSC MTS AUTO EXAM GENERATOR
Complete Automated System for SSC MTS 2026-2027 Exam Preparation

📋 PROJECT STRUCTURE & DOCUMENTATION
"""

# ============================================
# ARCHITECTURE OVERVIEW
# ============================================

PROJECT_STRUCTURE = """

📁 Ssc-mts-exam-generator/
│
├── 📂 src/
│   ├── 📂 tools/
│   │   ├── 📐 maths_tool.py
│   │   │   ├── MathsQuestionGenerator (AI-powered)
│   │   │   ├── MathsPDFExtractor (OCR support)
│   │   │   └── MathsTool (main class)
│   │   │
│   │   ├── 🧠 reasoning_tool.py
│   │   ├── 📰 current_affairs_tool.py
│   │   └── 📖 english_tool.py
│   │
│   ├── 📂 core/
│   │   ├── test_generator.py (Generate papers & sets)
│   │   ├── question_manager.py (CRUD operations)
│   │   └── database.py (MongoDB connections)
│   │
│   ├── 📂 api/
│   │   ├── app.py (FastAPI application)
│   │   ├── routes.py (API endpoints)
│   │   └── middleware.py (Auth, CORS)
│   │
│   ├── 📂 frontend/
│   │   ├── React components
│   │   └── UI/UX
│   │
│   └── models.py (Data models)
│
├── 📂 data/
│   ├── raw_papers/ (Downloaded PDFs)
│   ├── extracted_questions/ (Extracted from PDFs)
│   ├── generated_questions/ (AI generated)
│   └── mock_tests/ (Generated test papers)
│
├── 📂 scripts/
│   ├── init_db.py (Database setup)
│   ├── download_papers.py (Auto-download)
│   ├── extract_questions.py (Extract from PDFs)
│   └── generate_tests.py (Generate mock tests)
│
├── config.py (Global configuration)
├── requirements.txt (Python dependencies)
├── README.md (Project documentation)
├── .env.example (Environment variables template)
└── main.py (Entry point)

"""

# ============================================
# WORKFLOW & DATA FLOW
# ============================================

WORKFLOW = """

┌─────────────────────────────────────────────────────────────┐
│                     DATA COLLECTION PHASE                   │
└─────────────────────────────────────────────────────────────┘

1️⃣  DOWNLOAD SSC MTS PAPERS
    ├─ From SSC Official Website
    ├─ From Question Banks (Stored PDFs)
    └─ From Previous Year Papers Repository
    
2️⃣  EXTRACT QUESTIONS
    ├─ PDF Parsing (PyPDF2)
    ├─ OCR Processing (Tesseract/PaddleOCR)
    ├─ Text Cleaning & Normalization
    └─ Store in Database

3️⃣  QUESTION CLASSIFICATION
    ├─ Subject Detection (NLP)
    ├─ Topic Classification (ML)
    ├─ Difficulty Assessment
    └─ Metadata Extraction (Year, Session, etc.)

┌─────────────────────────────────────────────────────────────┐
│              AI QUESTION GENERATION PHASE                   │
└─────────────────────────────────────────────────────────────┘

4️⃣  PATTERN ANALYSIS
    ├─ Analyze 10-15 years of papers
    ├─ Identify question types & patterns
    ├─ Extract difficulty distribution
    └─ Learn question structure

5️⃣  AI QUESTION GENERATION
    ├─ Use GPT/Claude API for content
    ├─ Maintain SSC MTS difficulty level
    ├─ Generate Hindi & English versions
    ├─ Auto-validate generated questions
    └─ Store in database

6️⃣  DATABASE UPDATE
    ├─ Merge extracted + generated questions
    ├─ Remove duplicates
    ├─ Index by subject/topic
    └─ Ready for paper generation

┌─────────────────────────────────────────────────────────────┐
│                 PAPER GENERATION PHASE                      │
└─────────────────────────────────────────────────────────────┘

7️⃣  GENERATE MOCK TESTS
    ├─ Full Paper (100 Q) - Session-I & II
    ├─ Subject-wise Sets (25 Q each)
    ├─ Topic-wise Practice Sets
    ├─ Difficulty-balanced distribution
    └─ Randomized question order

8️⃣  EXPORT IN MULTIPLE FORMATS
    ├─ PDF (Printable)
    ├─ JSON (API/Web)
    ├─ CSV (Excel)
    ├─ Web Interface (Interactive)
    └─ Mobile App (React Native)

"""

# ============================================
# 4 MAIN TOOLS - DETAILED DESCRIPTION
# ============================================

TOOLS_DESCRIPTION = """

🔵 TOOL-1: MATHS TOOL (📐 maths_tool.py)
═══════════════════════════════════════════════════════════════

Subjects:
  ✓ Number System
  ✓ Fractions & Decimals
  ✓ LCM & HCF
  ✓ BODMAS
  ✓ Percentage
  ✓ Ratio & Proportion
  ✓ Profit, Loss & Discount
  ✓ Simple Interest
  ✓ Time & Work
  ✓ Speed, Time & Distance
  ✓ Mensuration
  ✓ Lines & Angles
  ✓ Data Interpretation

Classes:
  - MathsQuestionGenerator
    └─ generate_questions(topic, difficulty, count, language)
  
  - MathsPDFExtractor
    └─ extract_from_pdf(pdf_path)
    └─ extract_from_image(image_path)
  
  - MathsTool (Main)
    └─ run()

Features:
  ✅ Extract from previous year papers
  ✅ AI generate new questions
  ✅ Bilingual (Hindi/English)
  ✅ 3-level difficulty
  ✅ Answer keys with explanations


🟣 TOOL-2: REASONING TOOL (🧠 reasoning_tool.py)
═══════════════════════════════════════════════════════════════

Topics:
  ✓ Alpha-Numeric Series
  ✓ Coding-Decoding
  ✓ Analogy
  ✓ Classification
  ✓ Directions & Distance
  ✓ Order & Ranking
  ✓ Blood Relations
  ✓ Venn Diagrams
  ✓ Mathematical Operations
  ✓ Non-Verbal Reasoning
  ✓ Age Problems

Similar structure to Maths Tool


🟠 TOOL-3: GENERAL AWARENESS TOOL (📰 current_affairs_tool.py)
═══════════════════════════════════════════════════════════════

Topics:
  ✓ History (Ancient, Medieval, Modern India)
  ✓ Geography (Physical, Political, Climate)
  ✓ Polity & Constitution
  ✓ Economics
  ✓ Physics, Chemistry, Biology
  ✓ Art & Culture
  ✓ Books & Authors
  ✓ Sports
  ✓ Awards & Honors
  ✓ Current Affairs (Last 12 months)

Features:
  ✅ Extract from SSC previous papers
  ✅ Scrape current affairs from news
  ✅ Generate CA questions automatically
  ✅ Regular database updates


🟢 TOOL-4: ENGLISH TOOL (📖 english_tool.py)
═══════════════════════════════════════════════════════════════

Topics:
  ✓ Vocabulary (Synonyms, Antonyms, Idioms)
  ✓ Grammar (Parts of Speech, Tenses, SVA)
  ✓ Sentence Correction (Error Spotting)
  ✓ Fill in the Blanks
  ✓ Reading Comprehension
  ✓ Cloze Test

Features:
  ✅ Extract from papers
  ✅ Generate grammar exercises
  ✅ Reading comprehension passages
  ✅ Auto-generate questions from passages

"""

# ============================================
# SESSION STRUCTURE
# ============================================

SESSIONS = """

📘 SESSION-I (Qualifying - No Negative Marking)
═══════════════════════════════════════════════════════════════
Total Questions: 100
Total Marks: 100
Duration: 2 hours
Negative Marking: NO (0 marks for wrong answer)
Purpose: Qualifying threshold

Distribution:
  ├─ Maths: 25 Questions (25 Marks)
  ├─ Reasoning: 25 Questions (25 Marks)
  ├─ General Awareness: 25 Questions (25 Marks)
  └─ English: 25 Questions (25 Marks)

Difficulty Distribution:
  ├─ Easy: 33%
  ├─ Medium: 34%
  └─ Hard: 33%

Passing Criteria: ~30-35% marks required


📙 SESSION-II (Merit Deciding - 1-Mark Negative Marking)
═══════════════════════════════════════════════════════════════
Total Questions: 100
Total Marks: 100
Duration: 2 hours
Negative Marking: YES (1-mark deducted for wrong answer)
Purpose: Decides final merit list

Same distribution as Session-I

Difficulty Distribution:
  ├─ Easy: 30%
  ├─ Medium: 40%
  └─ Hard: 30%

"""

# ============================================
# OUTPUT FORMATS
# ============================================

OUTPUT = """

1️⃣  PDF FORMAT
    ├─ Professional layout
    ├─ Question numbers & marks
    ├─ Multiple choice options
    ├─ Answer key at the end
    ├─ Printable format
    └─ File: mock_test_session1.pdf

2️⃣  JSON FORMAT
    ├─ Structured data
    ├─ API integration ready
    ├─ Include metadata
    └─ File: mock_test_session1.json

3️⃣  CSV FORMAT
    ├─ Excel compatible
    ├─ Separate columns for Q, Options, Answer
    ├─ Easy to import in spreadsheets
    └─ File: mock_test_session1.csv

4️⃣  WEB INTERFACE
    ├─ Interactive exam interface
    ├─ Timer
    ├─ Question navigator
    ├─ Real-time results
    └─ Performance analytics

5️⃣  MOBILE APP
    ├─ React Native app
    ├─ Offline support
    ├─ Sync with web
    └─ Performance tracking

"""

# ============================================
# QUICK START GUIDE
# ============================================

QUICK_START = """

🚀 INSTALLATION & SETUP
═══════════════════════════════════════════════════════════════

1. Clone Repository:
   $ git clone https://github.com/mekonhu325-rgb/Ssc-mts-exam-generator.git
   $ cd Ssc-mts-exam-generator

2. Create Virtual Environment:
   $ python -m venv venv
   $ source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install Dependencies:
   $ pip install -r requirements.txt

4. Setup Environment Variables:
   $ cp .env.example .env
   # Edit .env with your settings

5. Initialize Database:
   $ python scripts/init_db.py


📐 GENERATE MATHS TEST
═══════════════════════════════════════════════════════════════

from src.tools.maths_tool import MathsTool
from config import DifficultyLevel

# Initialize tool
tool = MathsTool()

# Generate 25 questions
questions = tool.generator.generate_questions(
    topic="Percentage",
    difficulty=DifficultyLevel.MEDIUM,
    count=25,
    language="Hindi"
)

# Generate full test
from src.core.test_generator import TestPaperGenerator

gen = TestPaperGenerator()
paper = gen.generate_full_mock_test(session="SESSION_1", language="Hindi")

# Export
from src.core.test_generator import TestPaperExporter
exporter = TestPaperExporter()
exporter.export_to_pdf(paper, "mock_test.pdf")
exporter.export_to_json(paper, "mock_test.json")


🌐 RUN WEB SERVER
═══════════════════════════════════════════════════════════════

$ python main.py
# Server starts at http://localhost:8000

# API Documentation
http://localhost:8000/docs

"""

print(PROJECT_STRUCTURE)
print(WORKFLOW)
print(TOOLS_DESCRIPTION)
print(SESSIONS)
print(OUTPUT)
print(QUICK_START)
