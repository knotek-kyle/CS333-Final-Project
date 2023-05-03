FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/connect4

COPY src/main.py ./
COPY src/checkWins.py ./
COPY src/printBoard.py ./
COPY src/test.py ./
COPY src/testScript.txt ./

CMD [ "python3", "./main.py"]

