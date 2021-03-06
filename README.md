# FIR Classifier

![Sample FIR](assets/fir.jpg?raw=true "FIR")

This is the prototype developed for the classification of FIRs written in the language Kannada, it is deployed at : https://fir-classification.herokuapp.com/

### Working model

- Page to enter the case of the text

![Enter Case Text](assets/text.PNG?raw=true "Case text")

- Page to upload the PDF

![Upload Case File](assets/upload.PNG?raw=true "Case file")

- Sample case statement : XYZ received a call that he had got a job offer and was asked to send his personal documents and money after which he was not given a job.The classification is aptly obtained as the type JOB SCAM

![Sample Case Text](assets/sample_case.PNG?raw=true "Sample case text")

### Local Setup

Steps to follow to locally setup the project
  - Ensure to have Python with version >= 3.6
  - Preferably create a virtual environment
  - Clone the repository
  - Install all the dependencies by ```pip install -r requirements.txt```
  - To install ```POPPLER``` one of the dependencies, this article can be followed for those on Windows : https://newbedev.com/how-to-install-poppler-on-windows, for those on Ubuntu or Mac OS this canbe followed : https://pdf2image.readthedocs.io/en/latest/installation.html
  - Run ```streamlit run app.py``` from the root directory and open ```PORT 8501```

### Deployment
 
 In order to deploy this application, I have compiled all the steps in a blog 
 
 https://namyalg.medium.com/deploy-a-streamlit-app-on-heroku-with-ocr-c0ec2a3dab2e
