import os
import streamlit as st
from PIL import Image
from app_funcs import *

st.set_page_config(
    page_title="ISR using ESRGAN",
    page_icon="π«",
    layout="centered",
    initial_sidebar_state="auto",
)

upload_path = "uploads/"
download_path = "downloads/"

main_image = Image.open('static/compare.png')

st.image(main_image,use_column_width='auto')
st.title("π¨βπ»π¨βπ»IMAGE SUPER RESOLUTIONπ¨βπ»π¨βπ»") 
model_name = st.radio("Choose Model for Image Super Resolution", ('ESRGAN model β', 'PSNR-oriented model β'))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('static/background.png')    

st.info('β¨ Supports all popular image formats π· - PNG, JPG, BMP π')
uploaded_file = st.file_uploader("Upload Image π", type=["png","jpg","bmp","jpeg"])

if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        with st.spinner(f"Working... π«"):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            st.image(uploaded_image, caption='This is the original image π')
            downloaded_image = os.path.abspath(os.path.join(download_path,str("output_"+uploaded_file.name)))

            model = instantiate_model(model_name)
            image_super_resolution(uploaded_image, downloaded_image, model)
            print("Output Image: ", downloaded_image)
            final_image = Image.open(downloaded_image)
            print("Opening ",final_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your final image looks like π')
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                    if st.download_button(
                                            label="Download Output Image π·",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/jpg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                    if st.download_button(
                                            label="Download output Image π·",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/jpeg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                    if st.download_button(
                                            label="Download output Image π·",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/png'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                    if st.download_button(
                                            label="Download output Image π·",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/bmp'
                                         ):
                        download_success()
else:
    st.warning('β  Please upload your Image file π―')

st.markdown("<br><hr><center>Made with β€οΈ by <a href='mailto:thucdangvan020999@gmail.com?subject=ISR using ESRGAN WebApp!&body=Please specify the issue you are facing with the app.'><strong>LUU TIEN DAT</strong></a></center><hr>", unsafe_allow_html=True)
