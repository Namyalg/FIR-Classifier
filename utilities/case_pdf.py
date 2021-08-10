'''This file is used to upload the FIR case file,
   Extract the exact content of the case and
   provide its classification
'''

from PIL import Image 
import pytesseract 
import sys 
import pdf2image
from pdf2image import convert_from_bytes
import streamlit as st
import os
import pickle
import csv
#This API is used to translate text from Kannada to English
from google_trans_new import google_translator
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

def extract_text(file_path):
    '''
        This function is used to convert the pdf file to an image
        and extract the text of the case 
    '''
    PDF_file = file_path
    page_count = 0
    # Store all the pages of the PDF in translated_text variable 
    pages = convert_from_bytes(PDF_file, output_folder = ".") 
    images = []
    image_counter = 1
    complete_text = ""
    for page in pages:
      filename = "page_" + str(image_counter) + ".jpg"
      st.write(filename)
      page.save(filename, 'JPEG')
      images.append(filename)
      st.spinner(text = 'In progress...')
      text = pytesseract.image_to_string(filename, lang="kan")
      complete_text += text
      image_counter += 1
    FIR_starts = 0
    FIR_ends = 0
    counter = 0
    for line in complete_text.splitlines():
      counter += 1
      if 'ಪ್ರಥಮ ವರ್ತಮಾನ ವರದಿಯ ವಿವರಗಳು' in line:
        FIR_starts = counter
      if 'ತೆಗೆದುಕೊಂಡ ಕ್ರಮ' in line:
        FIR_ends = counter
    FIR_content = (" ".join(complete_text.strip("\n").splitlines()[FIR_starts - 1 : FIR_ends]))    
    for img in images:
        os.remove(img)
    return(FIR_content)

def translate_text(row):
    translator = google_translator()
    translated_text = translator.translate(row, lang_tgt='en')
    start = translated_text.find("Report")
    end = translated_text.rfind("11")
    return translated_text[start + 6 : end]

def upload_file():
    st.title("First Information Report Classifier")
    uploaded_file = st.file_uploader("Upload Files", type='pdf')
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write("This will take translated_text few minutes to process \n") 
        kannada_text = (extract_text(uploaded_file.getvalue()))
        st.write("The case content in kannada is \n")
        print(kannada_text)
        if kannada_text == "":
            st.write("Empty")
        st.write(kannada_text)
        st.write("The case content in english is \n")
        english_text = translate_text(kannada_text)
        st.write(english_text)
        case_content = english_text
        if st.button("Predict"):
            result = classify_utterance(case_content)
            st.success('The case belongs to class {}'.format(result))
    return 
