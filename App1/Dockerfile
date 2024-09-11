FROM node:20-alpine
FROM python:3.9-alpine

WORKDIR /flask_react_app

COPY Frontend/package*.json .

RUN npm install

COPY Backend/requirements.txt .

RUN pip install -r requirements.txt

COPY . .



CMD ["npm", "run", "dev"]






















