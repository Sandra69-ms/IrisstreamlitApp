import streamlit as st
import pickle

model = pickle.load(open("model/model_final.pkl", 'rb'))

st.title('APP FOR IRIS DATASET')

st.write('From messy data to  smart decision')

# st.text_input('sepal_width')
# st.text_input('sepal_length')
# st.text_input('petal_length')
# st.text_input('petal_width')

# st.button('Submit')

with st.form('Iris_app_form'):
    pi= st.number_input("Enter Petal Length")
    pw= st.number_input("Enter Petal Width")
    sl= st.number_input("Enter Sepal Length")
    sp= st.number_input("Enter Sepal Width")
    submitted = st.form_submit_button('predict Species')


if submitted:
    prediction = model.predict([[pi,pw,sl,sp]])
    st.success(f'Prediction is {prediction[0]}')

    species_map = {
        0: 'Iris-setosa',
        1: 'Iris-versicolor',
        2: 'Iris-virginica'
    }
    predicted_class = species_map.get(prediction[0],'Unknown species')
    st.success(f"The predicted Iris species is: {predicted_class}")

    if predicted_class == "Iris-setosa":
        st.image("images/irissetosa.jpg", caption="Iris-Setosa", use_container_width=True)
    elif predicted_class == "Iris-versicolor":
        st.image("images/irisversicolor.jpg", caption="Iris-Versicolor", use_container_width=True)
    elif predicted_class == "Iris-virginica":
        st.image("images/irisvirginica.jpeg", caption="Iris-Virginica", use_container_width=True)
    else:
        st.warning("No image available for this prediction.")