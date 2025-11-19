from fastapi import FastAPI
import time, random, uuid

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/run-task")
def run_task():
    task_id = str(uuid.uuid4())
    duration = random.uniform(2.0, 5.0)
    time.sleep(duration)
    return {"task_id": task_id, "duration_sec": duration}

@app.get("/metrics")
def metrics():
    return "app_requests_total 1\n"
