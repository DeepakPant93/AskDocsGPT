# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.


import logging
import os

from ..core.context import request_id_context


# Add the request ID filter to add request ID to the logs
class RequestIDLogFilter(logging.Filter):
    def filter(self, record):
        # Get the current request ID from the context (if available)
        request_id = request_id_context.get(None)
        record.request_id = request_id if request_id else "N/A"
        return True


# Function to configure the logger
def setup_logger():
    # Ensure the directory exists
    log_dir = '/tmp/askdocsgpt'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("ask_docs_client_logger")
    logger.setLevel(logging.INFO)

    # StreamHandler for console logging
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # FileHandler for logging to a file
    file_handler = logging.FileHandler(f'{log_dir}/client.log')
    file_handler.setLevel(logging.INFO)

    # Custom log format that includes request_id
    formatter = logging.Formatter(
        '%(asctime)s - %(request_id)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s'
    )

    # Set formatter for both handlers
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add custom filter for request_id to both handlers
    stream_handler.addFilter(RequestIDLogFilter())
    file_handler.addFilter(RequestIDLogFilter())

    # Add handlers to logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()
