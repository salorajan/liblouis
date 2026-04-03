import streamlit as st
import sys
import os

# 1. Tell Python to look in the 'python' folder for our new module
sys.path.append(os.path.join(os.getcwd(), 'python'))

import brl_louis as louis

st.set_page_config(page_title="Accessible Braille Studio", layout="wide")
st.title("1. Accessible Braille Studio: Multi-Language BRF")

if 'brf_result' not in st.session_state:
    st.session_state.brf_result = None

with st.sidebar:
    st.header("Settings")
    table_option = st.selectbox("Select Language Table", [
        "en-ueb-g2.ctb", "en-us-g1.ctb", "en-gb-g2.ctb", 
        "es-g1.ctb", "he-il.ctb", "ta.ctb", "en-ueb-g1.ctb"
    ])
    st.info("Refer to README for language table details.")

mode = st.radio(
    "2. Select Action Mode",
    ["Convert Text to Braille", "Convert Braille to Text"],
    index=0
)

uploaded_file = st.file_uploader("3. Upload .txt or .brf file", type=["txt", "brf"])
input_text = ""
if uploaded_file:
    input_text = uploaded_file.getvalue().decode("utf-8", errors="ignore")
else:
    input_text = st.text_area("4. Or Enter Content Manually", height=200)

if st.button("5. Run Conversion"):
    if input_text:
        try:
            if "Text to Braille" in mode:
                raw_brf = louis.translateString([table_option], input_text)
                st.session_state.brf_result = raw_brf[0] if isinstance(raw_brf, tuple) else raw_brf
            else:
                raw_text = louis.backTranslate([table_option], input_text)
                st.session_state.brf_result = raw_text[0] if isinstance(raw_text, tuple) else raw_text
        except Exception as e:
            st.error(f"Translation Error: {e}")
    else:
        st.warning("Input is empty.")

if st.session_state.brf_result:
    st.subheader("6. Conversion Result")
    st.code(st.session_state.brf_result, language=None)
    
    file_ext = ".brf" if "Text to Braille" in mode else ".txt"
    st.download_button(
        label=f"7. Download {file_ext} File",
        data=st.session_state.brf_result,
        file_name=f"output{file_ext}",
        key="brl_louis_v1"
    )
