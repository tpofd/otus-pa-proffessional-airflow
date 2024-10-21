# Курс Product Analytics Professional от Otus. Материалы с открытого занятия по Airflow

Учебные материалы с вебинаров и занятий по Airflow. [Ссылка на страницу курса](https://otus.ru/lessons/product-analytics-pro/)

## Установка Apache Airflow через [Docker](https://www.docker.com/)

1. Создадим папку для Airflow в корне пользовательской папки:
   ```
      cd ~
      mkdir airflow-docker
      cd airflow-docker
    ```
2. Затем с помощью команды curl скачаем конфигурационный файл docker-compose.yaml со стабильной сборкой Airflow
   ```
      curl -O https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
    ```
3. Подготовим окружение — создадим папки, в которых будут храниться даги, логи и плагины
   ```
      mkdir ./dags ./logs ./plugins
    ```
4. Все готово! Запускаем наш Docker
   ```
      docker-compose up airflow-init
      docker-compose up
    ```
