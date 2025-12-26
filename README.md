<h1 align="center">🕸️ HTML URL Extraction & Structural Analysis</h1>

<p align="center">
  <strong>Academic project</strong> for <em>Teoría de la Computación</em> (3rd year, Ingeniería Matemática).<br/>
  Extracts URLs from real and local HTML using <strong>two complementary approaches</strong>:
  <strong>BeautifulSoup</strong> (robust extraction) and <strong>PLY</strong> (lexer+parser for structural validation).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-0A7E8C?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PLY-Lexer%20%2B%20Parser-7B2CBF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/HTML-URL%20Extraction-E34F26?logo=html5&logoColor=white&style=for-the-badge"/>
  
  <a href="https://deepwiki.com/maria2332/Practica_teoria_computacion" target="_blank">
    <img src="https://img.shields.io/badge/DeepWiki-Documentation-purple?style=for-the-badge"/>
  </a>
</p>

---

## 📚 Project Documentation (External)

An automatically generated documentation view of this repository is available via DeepWiki:

👉 https://deepwiki.com/maria2332/Practica_teoria_computacion

--- 

## 👩‍🎓 Academic Context

- **Student:** María Arribas Ballesteros  
- **Degree:** Ingeniería Matemática (3rd year)  
- **Course:** Teoría de la Computación  

This project explores two different ways of analyzing HTML documents:

1. **BeautifulSoup** → tolerant, fast extraction (handles messy HTML).
2. **PLY (Lexer + Parser)** → stricter syntactic analysis (detects structural issues and tag balancing).

---

## 🎯 Objectives

- Extract **URLs** from:
  - Anchor tags: `<a href="...">`
  - Image tags: `<img src="...">`
- Support:
  - **Local HTML files**
  - **Real webpages** (online)
- Compare approaches:
  - **Extraction reliability**
  - **HTML structural validation**
  - **Tag balancing detection** (PLY)

---

## 🧠 Project Overview

### ✅ BeautifulSoup (bs4_extractor.py)
- Flexible parsing (tolerant to malformed HTML).
- Focus: **fast URL extraction** + basic tag statistics.
- Output:
  - Console summary
  - `urls_bs4_extraidas.txt`

### ✅ PLY Lexer+Parser (main.py + lexer.py + parser.py)
- Formal lexical + syntactic analysis.
- Focus: **URL extraction + structural validation**
- Reports:
  - Unbalanced / mismatched tags
  - Structural inconsistencies
- Output:
  - Console report
  - `urls_extraidas.txt`

---

## 📁 Repository Structure

```text
proyecto/
├── bs4_extractor.py
├── main.py
├── lexer.py
├── parser.py
├── prueba1.html
├── prueba2.html
├── prueba3.html
├── prueba4.html
├── prueba5.html
├── prueba6.html
└── README.md
````

---

## ⚙️ Requirements

* **Python 3.x**
* Install dependencies:

```bash
pip install requests beautifulsoup4 ply
```

> Ensure `lexer.py` and `parser.py` are in the same directory as `main.py`.

---

## ▶️ How to Run

### 1) BeautifulSoup analysis

Runs tolerant parsing and extraction.

```bash
python bs4_extractor.py
```

**Output:**

* `urls_bs4_extraidas.txt`
* Console extraction summary

---

### 2) PLY analysis (Lexer + Parser)

Runs strict parsing and reports structural issues.

```bash
python main.py
```

**Output:**

* `urls_extraidas.txt`
* Console report including **tag balancing / structural errors**

---

## 📌 Notes & Comparison

| Feature                  | BeautifulSoup | PLY (Lexer + Parser)  |
| ------------------------ | ------------- | --------------------- |
| Robust to malformed HTML | ✅ Yes         | ❌ No (reports errors) |
| Speed / ease of use      | ✅ High        | ⚠️ Medium             |
| URL extraction           | ✅ Yes         | ✅ Yes                 |
| Structural validation    | ❌ No          | ✅ Yes                 |
| Tag balancing detection  | ❌ No          | ✅ Yes                 |

**Recommended workflow:**
Use **BeautifulSoup** for quick extraction and **PLY** for structural validation.

---

## 🔍 Final Remarks

This repository demonstrates how different parsing strategies lead to different outcomes:

* **BeautifulSoup** prioritizes extraction robustness.
* **PLY** prioritizes formal correctness and structural consistency.

Together, they provide a complementary approach to HTML analysis.
