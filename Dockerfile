FROM python:alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python3"]
CMD ["python3", "migrate"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
