FROM python:3.5

WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

#ENV DISPLAY :0

COPY . .

CMD ["python", "main.py"]
