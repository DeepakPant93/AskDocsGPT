# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


import logging

from ..core.context import request_id_context


# Add the request ID filter to add request ID to the logs
class RequestIDLogFilter(logging.Filter):
    def filter(self, record):
        # Get the current request ID from the context (if available)
        request_id = request_id_context.get(None)
        record.request_id = request_id if request_id else "N/A"
        return True


def setup_logger():
    logger = logging.getLogger("ask_docs_client_logger")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    # Custom log format that includes request_id
    formatter = logging.Formatter(
        '%(asctime)s - %(request_id)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s'
    )
    handler.setFormatter(formatter)

    # Add the custom filter to include request_id in every log entry
    handler.addFilter(RequestIDLogFilter())

    logger.addHandler(handler)
    return logger


logger = setup_logger()
