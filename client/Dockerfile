# Stage 1: Build the wheel file
FROM python:3.9-slim AS builder

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
FROM python:3.9-slim

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

# Define environment variable
ENV NAME ask-docs-client

# Expose port 8502 for Streamlit
EXPOSE 8502

# Run the app when the container launches
CMD ["streamlit", "run", "main.py", "--server.port", "8502", "--server.address", "0.0.0.0"]
