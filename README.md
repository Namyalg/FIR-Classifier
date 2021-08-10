# FIR Classifier
- This is the prototype developed for the classification of FIRs written in the language Kannada 


### Working model

The prototype is deployed at : https://predict-fir.herokuapp.com

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
  - Run ```streamlit run app.py``` from the root directory and open ```PORT 8501```

### Deployment
 
 In order to deploy this application, I have compiled all the steps in a blog 
 
 https://namyalg.medium.com/deploy-a-streamlit-app-on-heroku-with-ocr-c0ec2a3dab2e
