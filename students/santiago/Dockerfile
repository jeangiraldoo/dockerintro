# Use lightweight Alpine Linux image for Python
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user and group for security best practices
RUN addgroup -S app && adduser -S app -G app

# Install wget required for the healthcheck
RUN apk add --no-cache wget

# Copy dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Create the log directory and assign permissions to the non-root user
RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

# Switch from root to the unprivileged user
USER app

# Expose the standard port requested by the lab
EXPOSE 8080

# Healthcheck configuration (Using 127.0.0.1 to prevent DNS resolution issues in Alpine)
HEALTHCHECK --interval=10s --timeout=3s --retries=5 --start-period=15s \
  CMD wget -qO- http://127.0.0.1:8080/health >/dev/null || exit 1

# Define the default command to start the Flask application
CMD ["python", "app.py"]