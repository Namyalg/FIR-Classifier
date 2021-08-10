#This file is used to accept the case text and provide a suitable classification

import pickle
import streamlit as st

def classify_utterance(utt):
    # load the vectorizer
    loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

    # load the model
    loaded_model = pickle.load(open('classification.model', 'rb'))

    # make a prediction
    return(loaded_model.predict(loaded_vectorizer.transform([utt])))

     
def enter_text():
    st.title("First Information Report Classifier")
    case_content = st.text_input("Case Content", "")
    if st.button("Predict"):
        result = classify_utterance(case_content)
        st.success('The case belongs to class {}'.format(result))
    return 
