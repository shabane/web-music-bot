FROM python:alpine
COPY . /var/code
RUN pip3 install -r /var/code/r.txt
WORKDIR /var/code
CMD [ "python3", "main.py"]