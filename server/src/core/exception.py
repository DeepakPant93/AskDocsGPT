# Copyright (c) 2024 Deepak Pant. All rights reserved.
# This file is part of the AskDocsGPT project.

from http import HTTPStatus

from fastapi import HTTPException


class ADException(HTTPException):
    """Custom Exception for Emailer related exceptions"""

    def __init__(self, status_code: HTTPStatus, detail: str):
        """Initialize the EMLException with the status code and detail message"""
        # Call the parent constructor (HTTPException)
        super().__init__(status_code=status_code.value, detail=detail)
        self.status_code = status_code
        self.detail = detail

    def to_dict(self):
        """Return the exception details as a dictionary (for JSON response)"""
        return {
            "status_code": self.status_code.value,
            "detail": self.detail
        }

    def __str__(self):
        """Return a human-readable string version of the exception"""
        return f"EMLException: {self.status_code.phrase} ({self.status_code.value}) - {self.detail}"
