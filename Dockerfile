# Base image 선택
FROM python:3.9.0

WORKDIR /home/

# RUN : command실행하여 image 안에 django source code가 들어감
RUN git clone https://github.com/rhceornd/pragmatic.git

WORKDIR /home/pramatic/

RUN pip install -r requirements.txt

# secretkey가 들어있는 .env file 생성
RUN echo "SECRET_KEY=django-insecure-ndl!g^fpl(txkez_$t313=qa3%h-uov1+p^ha9!n=o*rnqj+2$" > .env

# DB 연동
RUN python manage.py migrate

# port 번호 노출
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]