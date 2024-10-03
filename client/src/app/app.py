# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


import streamlit as st

from ..schema.v1.prompt_schema import AnswerResponse
from ..service.askdoc_service import AskDocsService

DEFAULT_OUTPUT_MSG: str = "There was a problem processing your request. Please try again after some time."


class AskDocsApp:

    def __init__(self):
        self.service = AskDocsService()

    async def start(self):
        ## streamlit framework
        st.title('AskDocsGPT')
        input_text = st.text_input("Search anything related to docs...")
        output = DEFAULT_OUTPUT_MSG
        source_docs = None

        if input_text:
            try:
                # Invoke the service to get the response containing the answer and source documents
                response: AnswerResponse = await self.service.ask(input_text)

                # Extract the answer and source documents from the response
                output = response.answer
                source_docs = response.source_documents
            except:
                st.error(output)
                return

            st.write(f"**{output}**")

            # Display the source documents in a more structured way
            if source_docs:
                st.markdown("_Source Documents:_")
                for idx, doc in enumerate(source_docs, start=1):
                    with st.expander(f"Document {idx}:"):
                        st.markdown(f"**Content**: {doc.get('page_content')}")
                        st.markdown(f"**Page**: {doc.get('metadata').get('page')}")
                        st.markdown(f"**Source**: {doc.get('metadata').get('source')}")

            st.markdown("---")
            st.caption("Powered by AskDocsGPT")
