FROM python:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "8000"]
