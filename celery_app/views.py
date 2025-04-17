from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add

import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .tasks import transcribe_audio_task

# Create your views here.
def testing(request):

    sum_from_tasks=add.delay()

    return HttpResponse("celery task done here ")





# views.py


@api_view(["POST"])
def upload_and_transcribe(request):
    file = request.FILES.get("audio")

    if not file:
        return Response({"error": "No audio file provided."}, status=status.HTTP_400_BAD_REQUEST)

    # Save uploaded file
    save_path = os.path.join("static", "audios", file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "wb+") as f:
        for chunk in file.chunks():
            f.write(chunk)

    # ✅ Start async task without passing task.id
    task = transcribe_audio_task.delay(save_path)
    
    return Response({
        "message": "Transcription started.",
        "task_id": task.id,
       
    }, status=status.HTTP_202_ACCEPTED)



from celery_app.utils.redis_util import redis_client


@api_view(["GET"])
def transcription_result(request, task_id):
    try:
        # Get list of transcribed chunks from Redis
        chunks = redis_client.lrange(f"transcription:{task_id}", 0, -1)
        
        # Fix: decode only if chunk is bytes
        chunks = [chunk.decode("utf-8") if isinstance(chunk, bytes) else chunk for chunk in chunks]
      

        # Check if transcription is done
        is_done = redis_client.get(f"transcription_done:{task_id}")
        is_done = bool(is_done)

        return Response({
            "transcription": " ".join(chunks),
            "done": is_done
        })

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
