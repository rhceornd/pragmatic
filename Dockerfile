# Base image 선택
FROM python:3.9.0

WORKDIR /home/

# RUN : command실행하여 image 안에 django source code가 들어감
RUN git clone https://github.com/rhceornd/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

# 포테이너를 통하기 때문에 캐시가 저장되어 있어 어떠한 변화를 줘야하기 떄문에 넣음
RUN pip install gunicorn

# secretkey가 들어있는 .env file 생성
RUN echo "SECRET_KEY=django-insecure-ndl!g^fpl(txkez_$t313=qa3%h-uov1+p^ha9!n=o*rnqj+2$" > .env

# DB 연동
RUN python manage.py migrate

# django에 필요한 static files를 모아 nginx에 동기화시키기 위한 명령어
RUN python manage.py collectstatic

# docker port 번호 노출
EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]