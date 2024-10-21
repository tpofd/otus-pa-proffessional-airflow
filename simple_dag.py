from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# задача с вычислениями
def compute(**kwargs):
    result = 42  # Например, результат сложных вычислений
    return result

# задачка которая принимает эти вычисления
def process_result(**kwargs):
    ti = kwargs['ti']
    result = ti.xcom_pull(task_ids='compute_task')
    print(f"Результат вычислений: {result}")

default_args = {  # Словарь с параметрами по умолчанию для задач в DAG.
    'owner': 'airflow',  # Указываем владельца задач.
    'start_date': datetime(2023, 10, 1),  # Указываем дату начала выполнения DAG.
    'retries': 1,  # Указываем количество попыток повторного выполнения задачи в случае неудачи.
}

# название нашего дага
dag = DAG('xcom_example', default_args=default_args, schedule_interval='@once')

# задаем первую задачку с python
compute_task = PythonOperator(
    task_id='compute_task',
    python_callable=compute,
    dag=dag,
)

# задаем вторую задачку с python
process_task = PythonOperator(
    task_id='process_task',
    python_callable=process_result,
    provide_context=True,
    dag=dag,
)

# задаем последовательность
compute_task >> process_task
