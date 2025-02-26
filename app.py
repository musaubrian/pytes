# import streamlit as st
# import pytesseract
# from PIL import Image
# import pyperclip
#
# st.title("Image Text Extractor")
#
# uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
#
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_container_width=True)
#
#     with st.spinner("Extracting text..."):
#         extracted_text = pytesseract.image_to_string(image)
#
#     st.subheader("Extracted Text")
#     if st.button(label="copy text"):
#         pyperclip.copy(extracted_text)
#         st.toast("Copied to clipboard!")
#     st.text_area(label="", extracted_text, height=250)

import streamlit as st
import pytesseract
from PIL import Image
import pyperclip
import subprocess
import io

st.title("Image Text Extractor")


# Function to get image from clipboard via `wl-paste`
def get_clipboard_image():
    try:
        result = subprocess.run(
            ["wl-paste", "--type", "image/png"], capture_output=True
        )
        if result.stdout:
            return Image.open(io.BytesIO(result.stdout))
    except Exception as e:
        st.toast(f"Clipboard image fetch failed: {e}")
    return None


uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if st.button("Paste Image"):
    image = get_clipboard_image()
else:
    image = None


# Load image from upload or clipboard
if uploaded_file:
    image = Image.open(uploaded_file)

if image:
    st.image(image, caption="Processed Image", use_column_width=True)
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image, config="--oem 1 --psm 6")

    st.subheader("Extracted Text")
    if st.button(label="Copy Text"):
        pyperclip.copy(extracted_text)
        st.toast("Copied to clipboard!")

    st.text_area(label="", value=extracted_text, height=250)
