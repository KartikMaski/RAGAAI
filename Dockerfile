# Use official Python slim image
FROM python:3.10-slim

# Avoid Python buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install OS dependencies for audio processing and ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg libsndfile1 curl && \
    apt-get clean

# Set work directory
WORKDIR /app

# Copy all files to /app in container
COPY . /app

# Upgrade pip and install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose streamlit default port
EXPOSE 8501

# Command to run your streamlit app
CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
