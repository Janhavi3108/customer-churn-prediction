# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn joblib pandas numpy scikit-learn

# Expose port 8000
EXPOSE 8000

# Run API server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
