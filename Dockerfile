FROM python:3.10-slim-buster
RUN apt-get update && apt-get -y install cmake
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "-u", "./main.py" ]