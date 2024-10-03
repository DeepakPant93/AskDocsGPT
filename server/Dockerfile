# Stage 1: Build the wheel file
FROM python:3.10-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Install setuptools and wheel for building the wheel file
RUN pip install --no-cache-dir setuptools wheel

# Build the wheel file
RUN python setup.py bdist_wheel

# Stage 2: Create the final image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the wheel file from the builder stage
COPY --from=builder /app/dist/*.whl /app/

# Install the wheel file
RUN pip install --no-cache-dir /app/*.whl

# Copy the application code into the final image
COPY . /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME ask-docs-server

# Run the app when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
