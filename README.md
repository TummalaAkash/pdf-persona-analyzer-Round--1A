# Adobe-India-Hackathon25  
## Challenge 1A – PDF Structure Extraction

This repository contains my solution for **Challenge 1A** of the Adobe India Hackathon 2025.

The goal was to extract the structural outline (like headings and subheadings) from a given PDF file and convert it into a clean, hierarchical **JSON** format.

---

## ✅ What I Did

I used **PyMuPDF** (`fitz`) to read and analyze each page of the PDF:

- Larger fonts and bold styles are treated as higher-level headings (like H1, H2, etc.)
- The script processes each page and captures all meaningful structure
- Output is saved in a clean JSON format with the page number, heading level, and text

---

## 📂 Input Format

All input PDF files should be placed inside the following directory:


---

## 🧾 Output Format

The output for each PDF is saved in the `Datasets/output/` directory in the following structure:

```json
{
  "title": "E0H1CM114",
  "outline": [
    {
      "level": "H1",
      "text": "Executive Summary",
      "page": 2
    },
    {
      "level": "H2",
      "text": "Goals and Objectives",
      "page": 3
    }
  ]
}
```

## 🐳 How to Run It (Using Docker)

### 🔧 Build the Docker Image

```bash
docker build --platform linux/amd64 -t heading_extractor:1a .
```

## ▶️ Run the Container
```bash
docker run --rm \
  -v ${PWD}/Datasets/input:/app/input \
  -v ${PWD}/Datasets/output:/app/output \
  --network none \
  heading_extractor:1a
```

## 📁 Project Structure

```bash
Challenge-1A/
├── Datasets/
│   ├── input/               # PDF input files go here
│   └── output/              # JSON outputs will be saved here
├── process_pdfs.py          # Main script to extract headings
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

## 📦 Dependencies

- Python 3.x  
- PyMuPDF (`fitz`)  
- Docker (for containerized execution)


** To install dependencies locally:**

```bash
pip install -r requirements.txt

```
