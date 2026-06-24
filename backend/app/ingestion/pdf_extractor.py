import fitz


def extract_text_from_pdf(pdf_path):
    try:
        text = ""

        with fitz.open(pdf_path) as pdf_document:
            for page in pdf_document:
                text += page.get_text("text",sort=True)

        return text

    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None