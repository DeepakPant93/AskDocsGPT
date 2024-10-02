# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from contextvars import ContextVar

# ContextVar to store the request_id for the current request
request_id_context: ContextVar[str] = ContextVar("request_id", default=None)
