FROM python:3.8
LABEL author="Mario"
WORKDIR /app
COPY ./requirements.txt requirements.txt
COPY . .
ENTRYPOINT ["python3"]
CMD ["app.py"] 