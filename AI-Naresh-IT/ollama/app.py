import streamlit as st
from ollama import Client

client = Client(host="http://localhost:11434")
st.set_page_config(page_title="Custom LLM model by Murali - Ollama", layout="centered")
st.title("Mr.Murali - Ollama app")

BUTTON_COLOR = "#0B7A75"        # button background colour
BUTTON_HOVER = "#95BB63"        # colour when the mouse is over the button
st.markdown(
    f"""
    <style>
    .st-key-gen_btn button {{
        background-color: {BUTTON_COLOR} !important;
        border: 1px solid {BUTTON_COLOR} !important;
    }}
    .st-key-gen_btn button:hover {{
        background-color: {BUTTON_HOVER} !important;
        border: 1px solid {BUTTON_HOVER} !important;
    }}
    .st-key-gen_btn button p {{
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

promt = st.text_area("Enter your prompt", height=200)
if st.button("Generate Response", type="primary", key="gen_btn"):
    if promt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Murali🔎Thinking..."):
            response = client.chat(
                # model="gemma3:270m",
                model = "deepseek-r1:1.5b",
                messages=[{"role": "user", "content": promt}
                ]
            )
            # resp_content = response.message.content
            # st.text(resp_content)
            st.success("Response generated successfully!")
            st.write(response["message"]["content"])
            # st.text_area("Response", value=response.message.content, height=200)