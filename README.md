# Optical Character Recognition App

This project demonstrates a simple web application built using Streamlit that allows users to upload images or PDF files (converted to images) and extract text from them using OCR (Optical Character Recognition).

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/rAvIkUmRa/OCR-App.git
   cd OCR-App


1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

2. Run the Streamlit app:

    ```bash
    streamlit run app.py

3. The app should open in your web browser. Upload an image or a PDF (converted to images) and click "Extract    Text" to see the extracted text.


Features

*Upload images or PDF files (converted to images) for text extraction.
*Extract text from the uploaded content using Tesseract OCR.
*Display extracted text and uploaded images in the app.


Dependencies

*Streamlit: Front-end web framework for building interactive web applications.
*pytesseract: Python wrapper for Google's Tesseract-OCR Engine.
*pdf2image: Library for converting PDF files to images.
*Pillow: Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.


Note

*The accuracy of text extraction depends on the quality of the images and content.
*OCR results might not be perfect, especially for complex or handwritten text.
*Please ensure that you have Tesseract installed and added to your system's PATH.


License

This project is licensed under the MIT License. See the LICENSE file for details.


Acknowledgements

*This project was inspired by the need to extract text from images and PDF files.
*Special thanks to the Streamlit community for providing an easy way to create interactive web apps.
*Tesseract OCR, pdf2image, and Pillow are used to enable text extraction and image processing.







