# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


class PromptInputSchema:
    question: str


class PromptOutputSchema:
    def __init__(self, answer: str):
        self.answer = answer
    # answer: str
