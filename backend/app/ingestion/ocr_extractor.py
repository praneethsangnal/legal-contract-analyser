import fitz
import numpy as np
import cv2
import gc

def extract_text_using_ocr(pdf_path):
    try:
        from rapidocr_onnxruntime import RapidOCR

        ocr_engine = RapidOCR()
        document = fitz.open(pdf_path)
        extracted_pages = []

        for page_number in range(len(document)):
            page = document.load_page(page_number)
            pix = page.get_pixmap(dpi=150)

            image = np.frombuffer(
                pix.samples,
                dtype=np.uint8
            ).reshape(
                pix.height,
                pix.width,
                pix.n
            )

            if pix.n == 4:
                image = cv2.cvtColor(
                    image,
                    cv2.COLOR_RGBA2BGR
                )
            else:
                image = cv2.cvtColor(
                    image,
                    cv2.COLOR_RGB2BGR
                )

            result, _ = ocr_engine(image)

            page_text = []
            if result:
                for line in result:
                    page_text.append(line[1])

            extracted_pages.append("\n".join(page_text))

            del pix
            del image
            del page
            gc.collect()

        document.close()
        return "\n\n".join(extracted_pages)

    except Exception as e:
        print(f"OCR Extraction Error: {e}")
        return None