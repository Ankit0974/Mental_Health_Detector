FROM python:3.10-slim

WORKDIR /app/backend

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend /app/backend
COPY model /app/model

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000