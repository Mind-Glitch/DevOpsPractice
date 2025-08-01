FROM python:3.14.0rc1-bookworm

LABEL maintainer="rosst0564@gmail.com"
ENV ADMIN="rosst"

RUN apk update && apk upgrade -y

WORKDIR /app

copy requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["uvicorn", "app:app"]