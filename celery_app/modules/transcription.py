import os
import whisperx
from celery_app.utils.redis_util import redis_client
# Load the model only once (improves speed)
model = whisperx.load_model(
    r"D:\Media_Github\media_live\media_content_analysis\models\models--Systran--faster-whisper-large-v2\snapshots\f0fe81560cb8b68660e564f55dd99207059c092e",
    device="cuda"
)
from pydub import AudioSegment


def split_audio(file_path, chunk_duration_ms=30_000):
    audio = AudioSegment.from_file(file_path)
    chunks = []
    base, _ = os.path.splitext(file_path)
    for i in range(0, len(audio), chunk_duration_ms):
        chunk = audio[i:i+chunk_duration_ms]
        chunk_path = f"{base}_chunk_{i//chunk_duration_ms}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)
    return chunks

# def transcribe_in_chunks(file_path):
#     chunks = split_audio(file_path)
#     for chunk in chunks:
#         audio = whisperx.load_audio(chunk)
#         result = model.transcribe(audio)
#         os.remove(chunk)


#         print("🧠 Chunk Transcription:")
#         for seg in result["segments"]:
#             print(seg["text"], end=" ")
#         print("\n" + "-"*60)




def transcribe_in_chunks(file_path, task_id=None):
    chunks = split_audio(file_path)

   # Or globally load for performance

    for idx, chunk in enumerate(chunks):
        try:
            audio = whisperx.load_audio(chunk)
            result = model.transcribe(audio)

            text = " ".join([seg["text"] for seg in result["segments"]])

            # Optional: publish to Redis if you want real-time frontend updates
            if task_id:
                redis_client.rpush(f"transcription:{task_id}", text)
       
            
            print("🧠 Chunk Transcription:")
            print(text)
            print("-" * 60)

        except Exception as e:
            print(f"❌ Error transcribing {chunk}: {e}")

        finally:
            try:
                os.remove(chunk)
                print(f"🗑️ Removed chunk: {chunk}")
            except Exception as e:
                print(f"⚠️ Failed to delete {chunk}: {e}")
