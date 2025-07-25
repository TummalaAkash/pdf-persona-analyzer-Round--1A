import os
import fitz  # PyMuPDF
import json


def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace(".pdf", "")
    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                spans = line.get("spans", [])
                if not spans:
                    continue

                text = "".join(span["text"] for span in spans).strip()
                if not text:
                    continue

                font_size = spans[0]["size"]
                font_flags = spans[0]["flags"]

                # Heuristic: size + boldness → H1, H2, H3
                if font_size > 16 or (font_flags & 2 and font_size > 14):
                    level = "H1"
                elif 13 < font_size <= 16:
                    level = "H2"
                elif 11 <= font_size <= 13:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num + 1
                })

    return {"title": title, "outline": outline}


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            result = extract_headings(pdf_path)
            json_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_dir, json_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
