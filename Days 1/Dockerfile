FROM python:3.12-slim

# container ma halne directory
WORKDIR /app

COPY requirements.txt .

#install requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy project basically git add.
COPY . .

EXPOSE 8000

# run the project
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
