import streamlit as st
from utils import prediction
from PIL import Image
# Set the page config


# set the title
st.title("Cat and Dog Classification")

# add a file uploader
upload_image=st.file_uploader("Upload Image: ")
if upload_image is not None:
    image=Image.open(upload_image)
    st.write(image)

if st.button("Classify"):
    y_pred = prediction(image=image)
    st.markdown(f"<h2 style='text-align: center; color: green;'>{y_pred}</h2>", unsafe_allow_html=True)

