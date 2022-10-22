FROM python:3.8
LABEL author="Mario"
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip uninstall -y PyYAML & pip install --ignore-installed PyYAML==5.3.1
COPY . .
ENTRYPOINT ["python3"]
CMD ["app.py"] 