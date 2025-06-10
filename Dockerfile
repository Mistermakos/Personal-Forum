FROM python:3.14-rc-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

#Installs all packages from requirements.txt, optimized 
RUN pip install -r requirements.txt

copy app/ ./

EXPOSE 5000

CMD ["python", "./main.py"]
