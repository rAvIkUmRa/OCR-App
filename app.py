import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import tempfile



def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text



def convert_pdf_to_images(uploaded_pdf):
    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_pdf.read())

    # Close the temporary PDF file
    temp_pdf.close()

    # Convert the temporary PDF file to images using pdf2image
    images = convert_from_path(temp_pdf.name, dpi=150, thread_count=4)

    # Remove the temporary PDF file
    import os
    os.unlink(temp_pdf.name)

    return images


def main():
    st.title("Text Extraction App")
    st.write("Upload an image or a PDF (converted to images) and click 'Extract Text' to extract text from it.")

    uploaded_file = st.file_uploader("Choose an image or PDF (images)", type=["jpg", "jpeg", "png", "pdf"])

    if uploaded_file is not None:
        if st.button("Extract"):
            if uploaded_file.type.startswith('image'):
                # Display the uploaded image
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)

                # Extract text from the image
                extracted_text = extract_text_from_image(image)
                st.write("Extracted Text:")
                st.write(extracted_text)
            elif uploaded_file.type == 'application/pdf':
                # Convert PDF to images using pdf2image and extract text
                images = convert_pdf_to_images(uploaded_file)
                extracted_texts = []
                for image in images:
                    extracted_text = extract_text_from_image(image)
                    extracted_texts.append(extracted_text)
                
                for page_num, text in enumerate(extracted_texts, start=1):
                    st.subheader(f"Page {page_num} Text:")
                    st.write(text)
            else:
                st.write("Unsupported file type. Please upload an image or PDF file (converted to images).")

if __name__ == "__main__":
    main()
