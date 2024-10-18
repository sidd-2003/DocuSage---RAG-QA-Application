# Use the official Python 3.10 image as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install PyTorch, torchvision, and torchaudio with CUDA 12.4 support
RUN pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124

# Install xformers with CUDA 12.4 support
RUN pip install -U xformers --index-url https://download.pytorch.org/whl/cu124

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV XFORMERS_FORCE_DISABLE_TRITON=1

# Run the application
CMD ["streamlit", "run", "app.py"]
