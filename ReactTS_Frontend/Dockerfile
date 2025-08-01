FROM node:24-alpine3.21

LABEL maintainer="rosst0564@gmail.com"
ENV ADMIN="rosst"

RUN apt update && apt upgrade -y
RUN npm install vite -y

WORKDIR /app

COPY . .


CMD["npm", "run", "dev"]