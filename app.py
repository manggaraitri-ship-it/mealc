import streamlit as st
from pypdf import PdfMerger
import io

st.title("Merge PDF")

uploaded_files = st.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    if st.button("Gabungkan PDF"):

        merger = PdfMerger()

        for pdf in uploaded_files:
            merger.append(pdf)

        output = io.BytesIO()

        merger.write(output)
        merger.close()

        output.seek(0)

        st.download_button(
            "Download PDF Gabungan",
            output,
            "merged_pdf.pdf",
            "application/pdf"
        )
