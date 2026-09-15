FROM python:3-slim

WORKDIR /app
RUN pip install --no-cache-dir --upgrade "fastapi[standard]"

COPY app.py .
EXPOSE 8000
CMD ["fastapi", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]
