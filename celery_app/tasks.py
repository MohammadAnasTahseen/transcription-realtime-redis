from celery import shared_task

@shared_task
def add():
    sum=0
    for i in  range(11):
        print("counitng-----------------------numbers",i)
        sum+=i


    print("sum",sum)

    return sum




# tasks.py
from celery import shared_task
from .modules.transcription import transcribe_in_chunks

@shared_task(bind=True)
def transcribe_audio_task(self, file_path):
    return transcribe_in_chunks(file_path, task_id=self.request.id)



    

