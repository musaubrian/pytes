import streamlit as st
import pytesseract
from PIL import Image
import pyperclip
import subprocess
import io
import numpy as np
import cv2

st.title("Image Text Extractor")


def preprocess_image(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    return Image.fromarray(thresh)


# get image from clipboard
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
    image = preprocess_image(image)
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image, config="--psm 6")

    st.subheader("Extracted Text")
    if st.button(label="Copy Text"):
        pyperclip.copy(extracted_text)
        st.toast("Copied to clipboard!")

    st.text_area(label="-", value=extracted_text, height=250)

    st.image(image, caption="Processed Image", use_container_width=True)
