import pymupdf  # PyMuPDF
import docx2txt
import tempfile
import csv

async def extract_text_from_file(uploaded_file):
    content = await uploaded_file.read()
    filename = uploaded_file.filename.lower()

    if filename.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        doc = pymupdf.open(tmp_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text

    elif filename.endswith(".docx"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        return docx2txt.process(tmp_path)

    elif filename.endswith(".txt"):
        return content.decode("utf-8")

    elif filename.endswith(".csv"):
        try:
            decoded = content.decode("utf-8").splitlines()
        except UnicodeDecodeError:
            decoded = content.decode("cp1252").splitlines()  # fallback encoding

        reader = csv.reader(decoded)
        text = "\n".join([" | ".join(row) for row in reader])
        return text


    else:
        return "Unsupported file format."

