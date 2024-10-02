# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


import streamlit as st

from ..service.askdoc_service import AskDocsService

DEFAULT_OUTPUT_MSG: str = "Search anything related to docs..."

class AskDocsApp:

    def __init__(self):
        self.service = AskDocsService()

    async def start(self):
        ## streamlit framework
        st.title('AskDocsGPT')
        input_text = st.text_input("Search anything related to docs...")
        output = DEFAULT_OUTPUT_MSG

        if input_text:
            output = await self.service.invoke(input_text)
        st.write(output)
