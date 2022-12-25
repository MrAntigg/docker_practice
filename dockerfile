FROM python:3
RUN pip3 install wget
ADD favicon.py /
CMD ["python", "./favicon.py"]