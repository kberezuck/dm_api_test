FROM python:latest

# Копирование исходного кода в тестах в образ
COPY . .
RUN pip3 install -r requirements.txt


#Запуск автотеста
CMD pytest /tests