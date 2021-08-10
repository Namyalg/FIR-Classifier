#the driver program

import streamlit as st
from utilities.multiapp import MultiApp
from utilities.case_text import enter_text
from utilities.case_pdf import upload_file

app = MultiApp()
app.add_app("Enter the text of the case content", enter_text)
app.add_app("Upload the case file", upload_file)
app.run()
