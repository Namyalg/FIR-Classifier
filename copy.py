import pickle
import streamlit as st

def classify_utterance(utt):
    # load the vectorizer
    loaded_vectorizer = pickle.load(open('vectorizer1.pickle', 'rb'))

    # load the model
    loaded_model = pickle.load(open('classification1.model', 'rb'))

    # make a prediction
    return(loaded_model.predict(loaded_vectorizer.transform([utt])))

     

st.title("First information Report")

case_content = st.text_input("Case Content", "")

if st.button("Predict"):
        result = classify_utterance(case_content)

        st.success('The output is {}'.format(result))

#text = "I was promised a job offer but was not given any offer and my details were stolen"
#text1 = "I purchased a washing machine which costed 200 thousand ruppes but was given the fake product"
